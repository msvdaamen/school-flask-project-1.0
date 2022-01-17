from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, EmailField, FileField

class UpdateMovieForm(FlaskForm):
    class Meta:
        csrf = False

    title = StringField('title', [validators.Optional()])
    cover = FileField('cover', [validators.Optional()])