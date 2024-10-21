import asyncio
import aiohttp
import logging

import click


from bovine.activitystreams import factories_for_actor_object
from bovine.clients import lookup_uri_with_webfinger

from ptpython.repl import embed

from .server import create_app, actor, actor_object, make_id

activity_factory, object_factory = factories_for_actor_object(
    actor_object, id_generator=make_id
)


@click.group()
@click.option(
    "--debug", is_flag=True, default=False, help="Sets the log level to debug."
)
def main(debug):
    """Command line to tool to manage a testing environment"""

    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


@main.command()
@click.option("--port", default=5000, help="Port the application runs on")
@click.option("--reload", default=False, is_flag=True, help="Enable auto reloading")
def serve(port, reload):
    """Serves the app from the bovine tutorial as
    a server"""
    app = create_app()
    app.run(port=port, host="0.0.0.0", use_reloader=reload)


def config(repl):
    repl.use_code_colorscheme("dracula")
    repl.enable_output_formatting = True


async def repl():
    print(
        "Relevant variables are actor, actor_object, activity_factory, object_factory."
    )

    async with aiohttp.ClientSession() as session:
        await actor.init(session=session)

        async def webfinger(acct_uri):
            domain = acct_uri.split("@")[1]
            actor_id, _ = await lookup_uri_with_webfinger(
                session, acct_uri, domain=f"http://{domain}"
            )
            return actor_id

        await embed(
            globals=globals(),
            locals=locals(),
            return_asyncio_coroutine=True,
            patch_stdout=True,
            configure=config,
        )


@main.command()
def shell():
    """Opens a REPL to perform actions using the [BovineActor][bovine.BovineActor]
    from the server tutorial"""
    asyncio.run(repl())


@main.command()
@click.option("--nano", help="Use nano editor", is_flag=True, default=False)
def edit(nano):
    """Allows one to edit the main server file"""

    editor = "nano" if nano else "vim"

    import subprocess

    subprocess.run(["apk", "add", editor])
    import bovine.testing.server

    subprocess.run([editor, bovine.testing.server.__file__])


if __name__ == "__main__":
    main()
