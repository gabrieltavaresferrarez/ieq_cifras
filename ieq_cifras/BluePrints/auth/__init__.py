import flask
from flask import Blueprint

from flask_login import LoginManager, login_user, current_user, logout_user, login_required

from ieq_cifras.models import User

login_manager = LoginManager()

bp_auth = Blueprint('auth', __name__, url_prefix='/', template_folder='templates')
from . import routes

def init_app(app:flask.Flask):
    app.register_blueprint(bp_auth)
    login_manager.login_view = 'auth.login'
    login_manager.login_login_messsage_category = 'info'
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    login_manager.init_app(app)