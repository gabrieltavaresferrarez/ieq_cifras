from flask import Flask
from dynaconf import Dynaconf



def create_app(settings:Dynaconf) -> Flask:
    app = Flask(__name__)

    return app