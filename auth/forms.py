from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, EmailField


class RegisterForm(FlaskForm):
    email = EmailField('Email', [validators.Length(min=6, max=35), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', [validators.DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField('Email Address', [validators.Length(min=6, max=35), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

