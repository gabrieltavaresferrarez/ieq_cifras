from flask import Blueprint

bp_cifra = Blueprint('cifra', __name__, url_prefix='/cifra', template_folder='templates')

from . import routes
def init_app(app):
    app.register_blueprint(bp_cifra)