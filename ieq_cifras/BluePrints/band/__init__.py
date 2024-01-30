from flask import Blueprint, Flask

bp_band = Blueprint('band', __name__, url_prefix='/band', template_folder='templates')
from . import routes

def init_app(app:Flask):
    app.register_blueprint(bp_band)