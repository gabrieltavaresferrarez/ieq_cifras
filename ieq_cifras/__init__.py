from flask import Flask
from dynaconf import Dynaconf

#Blueprints imports
from .BluePrints import config

def create_app(settings:Dynaconf) -> Flask:
    app = Flask(__name__)

    # config app
    config.init_app(app, settings)

    return app