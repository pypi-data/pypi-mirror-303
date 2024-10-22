
"""This module provides the RP To-Do CLI."""
import asyncio
# rptodo/cli.py

from typing import Optional

import typer

from zinley import __app_name__, __version__
from zinley import api_key, deployment_id, max_tokens, endpoint
from fsd.main import start

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return

@app.command("start")
def func_start(project_path, secret1, secret2, secret3):
    if authenticate(secret1, secret2, secret3):
        asyncio.run(start(project_path))
    else:
        exit(1)

def authenticate(secret1, secret2, secret3):
    if secret1 == "rignu2-tebkeb-gaqziX" and secret2 == "rugbo0-buzhox-zuWqak" and secret3 == "fydwum-soxdov-9tIzvy":
        return True
    else:
        return False
