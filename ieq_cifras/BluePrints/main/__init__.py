from flask import Blueprint, Flask

bp_main = Blueprint('main', __name__, url_prefix='/', template_folder='templates')
from . import routes

def init_app(app:Flask):
    app.register_blueprint(bp_main)