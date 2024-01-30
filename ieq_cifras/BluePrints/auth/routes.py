from . import bp_auth
from .forms import LoginForm, RegisterForm, RequestChangePasswordForm, ChangePasswordForm

from ieq_cifras.models import User
from ieq_cifras.Extensions.database import database

from flask import render_template, redirect, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required



@bp_auth.route('/login', methods = ['GET', 'POST'])
def login():
    #  verify if user is logged already
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
     # create form
    form_login = LoginForm()
    if request.method == 'GET': # when accessing the page
        return render_template('login.html', title='Login', form=form_login)
    
    elif request.method == 'POST': # when sending the form to login
        if form_login.validate_on_submit():
            user = User.query.filter_by(is_del=False).filter_by(email=form_login.email.data).first()
            if user:
                if check_password_hash(user.password, form_login.password.data):
                    login_user(user, remember=True)
                    flash(f'Usuário {user} loggado')
                    return redirect(url_for('auth.login'))
                else:
                    flash('Wrong password')
                    return redirect(url_for('auth.login'))
            else:
                flash('User not registered')
                return redirect(url_for('auth.login'))
        else:
            flash("Form didn't validate")
            return url_for('auth.login')

@bp_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@bp_auth.route('/register', methods = ['GET', 'POST'])
def register():
    #  verify if user is logged already
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    # create form
    form_register = RegisterForm()
    if request.method == 'GET': # when accessing the form
        return render_template('register.html', title='Login', form=form_register)
    
    elif request.method == 'POST': # when sending the form
        if form_register.validate_on_submit():
            if User.query.filter_by(is_del=False).filter_by(email=form_register.email.data).first():
                flash("Email already registered.")
                return url_for('auth.register')
            else:
                user = User(
                    username=form_register.username.data, 
                    email=form_register.email.data,
                    password=generate_password_hash(form_register.password.data)
                )
                database.session.add(user)
                database.session.commit()
                return redirect(url_for('auth.login'))
        else:
            flash("Form didn't validate")
            return redirect(url_for('auth.register'))


@bp_auth.route('/reset_password')
def reset_password():
    return 'reset_password'

@bp_auth.route('/request_reset_password')
def request_reset_password():
    return 'request_reset_password'