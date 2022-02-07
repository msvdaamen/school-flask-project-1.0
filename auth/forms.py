from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, EmailField


class RegisterForm(FlaskForm):
    email = EmailField('E-Mailadres', [validators.Length(min=6, max=35), validators.DataRequired()])
    password = PasswordField('Wachtwoord', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Herhaal Wachtwoord', [validators.DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField('E-Mailadres', [validators.Length(min=6, max=35), validators.DataRequired()])
    password = PasswordField('Wachtwoord', [validators.DataRequired()])

