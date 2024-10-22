"""
Load an application using the environement variable `PLASTER_URI`.
"""

import os
from typing import Any

import plaster

WSGIApp = Any


def load_app(plaster_uri: str | None) -> WSGIApp:
    if plaster_uri is None:
        raise LookupError("missing environment variable PLASTER_URI")

    loader = plaster.get_loader(plaster_uri)
    loader.setup_logging({})
    return loader.get_wsgi_app()


app = load_app(os.getenv("PLASTER_URI"))
