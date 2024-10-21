# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

"""The goal of the testing module is to provide
some examples of commonly used things to make writing
tests easier.


<!--
```
>>> import bovine.utils
>>> bovine.utils.now_isoformat = lambda: '2024-09-26T18:35:42Z'

```
-->

## Usage examples

For [public_key][bovine.testing.public_key] and [private_key][bovine.testing.public_key]

```pycon
>>> from bovine.crypto.helper import pem_private_key_to_pem_public_key
>>> pem_private_key_to_pem_public_key(private_key) == public_key
True

```

For [ed25519_key][bovine.testing.ed25519_key] and
[did_key][bovine.testing.did_key]

```pycon
>>> from bovine.crypto import private_key_to_did_key
>>> private_key_to_did_key(ed25519_key) == did_key
True

```


For [activity_factory][bovine.testing.activity_factory] see also
[ActivityFactory][bovine.activitystreams.activity_factory.ActivityFactory]

```pycon
>>> activity_factory.like("http://bovine.example").build()
{'@context': 'https://www.w3.org/ns/activitystreams',
    'type': 'Like',
    'actor': 'http://actor.example',
    'published': '2024-09-26T18:35:42Z',
    'object': 'http://bovine.example'}

```

For [object_factory][bovine.testing.object_factory] see also
[ObjectFactory][bovine.activitystreams.object_factory.ObjectFactory]
and the provided [note][bovine.testing.note]

```pycon
>>> object_factory.note(content="moo").build()
{'@context': 'https://www.w3.org/ns/activitystreams',
    'type': 'Note',
    'attributedTo': 'http://actor.example',
    'published': '2024-09-26T18:35:42Z',
    'content': 'moo'}

>>> note
{'@context': 'https://www.w3.org/ns/activitystreams',
    'type': 'Note',
    'attributedTo': 'http://actor.example',
    'to': ['https://www.w3.org/ns/activitystreams#Public'],
    'cc': ['http://actor.example/followers'],
    'published': '...',
    'content': 'moo'}


```

"""

from bovine.activitystreams.activity_factory import ActivityFactory
from bovine.activitystreams.object_factory import ObjectFactory

from .config import public_key as public_key_const, private_key as private_key_const

public_key = public_key_const
"""The public key corresponding to [private_key][bovine.testing.private_key]
"""

private_key = private_key_const
"""An RSA private key"""

ed25519_key = "z3u2Yxcowsarethebestcowsarethebestcowsarethebest"
"""An Ed25519 private key encoded in multibase"""

public_key_multibase = "z6MkekwC6R9bj9ErToB7AiZJfyCSDhaZe1UxhDbCqJrhqpS5"
"""A public ed25519 key encoded in multibase"""

did_key = f"did:key:{public_key_multibase}"
"""A did key"""

ecp256_key = "z42twTcNeSYcnqg1FLuSFs2bsGH3ZqbRHFmvS9XMsYhjxvHN"
"""A NIST P-256 private key"""

actor = {
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://w3id.org/security/v1",
    ],
    "publicKey": {
        "id": "http://actor.example#name",
        "owner": "http://actor.example",
        "publicKeyPem": public_key,
    },
    "id": "http://actor.example",
    "type": "Person",
    "inbox": "http://actor.example/inbox",
    "outbox": "http://actor.example/outbox",
    "followers": "http://actor.example/followers",
}
"""Example of an ActivityStreams Actor"""

activity_factory = ActivityFactory(actor)
"""The activity factory for the actor"""

object_factory = ObjectFactory(actor)
"""The object factory for the actor"""

note = object_factory.note(content="moo").as_public().build()
"""Example of a Note object"""
