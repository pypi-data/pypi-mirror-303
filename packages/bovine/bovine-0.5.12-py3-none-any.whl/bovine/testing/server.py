"""
This package contains a simple ActivityPub server for
testing purposes. See [Bovine - Tutorial-Server][https://bovine.readthedocs.io/en/latest/tutorials/server/].


Default variables are

```pycon
>>> hostname, port, handle_name
('bovine', 80, 'milkdrinker')

```

they can be set using `BOVINE_TEST_HOSTNAME`, `-_PORT`, `-_NAME`.

"""

import os
import secrets
import json

from quart import Quart, request

from bovine import BovineActor
from bovine.activitystreams import Actor
from bovine.crypto import build_validate_http_signature
from bovine.utils import webfinger_response_json

from .config import public_key, private_key


port = os.environ.get("BOVINE_TEST_PORT", 80)
hostname = os.environ.get("BOVINE_TEST_HOSTNAME", "bovine")
handle_name = os.environ.get("BOVINE_TEST_NAME", "milkdrinker")

actor_id = f"http://{hostname}/{handle_name}"
"""The actor id"""

webfinger_response = webfinger_response_json(f"acct:{handle_name}@{hostname}", actor_id)
"""The webfinger response"""

actor_object = Actor(
    id=actor_id,
    preferred_username=handle_name,
    name="The Milk Drinker",
    inbox=f"http://{hostname}/inbox",
    outbox=actor_id,
    public_key=public_key,
    public_key_name="main-key",
).build()


actor = BovineActor(
    actor_id=actor_id,
    public_key_url=f"{actor_id}#main-key",
    secret=private_key,
)


def make_id():
    return f"http://{hostname}/" + secrets.token_urlsafe(6)


def create_app():
    app = Quart(__name__)

    @app.before_serving
    async def startup():
        await actor.init()

    async def fetch_public_key(url):
        result = await actor.get(url)

        public_key = result["publicKey"]
        return public_key["publicKeyPem"], public_key["owner"]

    verify = build_validate_http_signature(fetch_public_key)

    @app.get("/.well-known/webfinger")
    async def webfinger():
        return webfinger_response

    @app.get("/" + handle_name)
    async def get_actor():
        return actor_object, 200, {"content-type": "application/activity+json"}

    @app.post("/inbox")
    async def post_inbox():
        controller = await verify(request)
        if not controller:
            return "ERROR", 401

        data = await request.get_json()
        print(f"Received in inbox from {controller}")
        print(json.dumps(data, indent=2))
        print()
        return "success", 202

    return app
