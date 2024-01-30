from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed

from ieq_cifras.models import User

class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, max=50)
        ]
    )
    password_confirm = PasswordField(
        'Password Confirm',
        validators=[
            DataRequired(),
            Length(min=8, max=50),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(is_del=False).filter_by(email=email.data).all():
            raise ValidationError("This email is taken. Choose other email.")


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, max=50)
        ]
    )
    submit = SubmitField('Login')

class RequestChangePasswordForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    submit = SubmitField('Send email')

    def validate_email(self, email):
        if not User.query.filter_by(is_del=False).filter_by(email=email.data).all():
            raise ValidationError("There is no accounte with this email registered")



class ChangePasswordForm(FlaskForm):
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, max=50)
        ]
    )
    password_confirm = PasswordField(
        'Password Confirm',
        validators=[
            DataRequired(),
            Length(min=8, max=50),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Register')
