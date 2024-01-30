from . import bp_main
from flask import render_template, redirect
from flask_login import current_user

@bp_main.route('/')
@bp_main.route('/home')
def home():
    return render_template('home.html', user=current_user)

@bp_main.route('/about')
def about():
    return render_template('about.html', user=current_user)