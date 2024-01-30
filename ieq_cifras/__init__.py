from flask import Flask
from dynaconf import Dynaconf

#Blueprints imports
from .BluePrints import config
from .BluePrints import main
from .BluePrints import cifra
from .BluePrints import auth
from .BluePrints import band

# Extensions imports
from .Extensions import database
from .Extensions import admin


def create_app(settings:Dynaconf) -> Flask:
    app = Flask(__name__)

    # config app
    config.init_app(app, settings)

    # Extensions
    database.init_app(app)
    admin.init_app(app) 
    

    # Blueprints
    main.init_app(app)
    cifra.init_app(app)
    band.init_app(app)
    auth.init_app(app)

    return app