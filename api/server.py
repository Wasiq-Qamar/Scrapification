from flask import Flask
from flask_restful import Api
from typing import List

from api.rotues import base

def get_api_server() -> Flask:
    """This server function configures the api server using the flask module"""
    app: Flask = Flask(__name__)
    api: Api = Api(app)

    # Manage Endpoints
    add_resource(api, base.ROUTES)

    return app


def add_resource(api: Api, routes: List[dict]) -> None:
    """This function adds resources to an Api object"""

    for resource in routes:
        api.add_resource(
            resource["resource"],
            *resource["endpoints"],
        )

    return