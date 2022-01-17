from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, EmailField, FileField

class CreateMovieForm(FlaskForm):
    class Meta:
        csrf = False

    cover = FileField('cover', [validators.DataRequired()])
    banner = FileField('banner', [validators.DataRequired()])
    title = StringField('title', [validators.DataRequired()])
    date = StringField('date', [validators.DataRequired()])


class UpdateMovieForm(FlaskForm):
    class Meta:
        csrf = False

    cover = FileField('cover', [validators.Optional()])
    banner = FileField('banner', [validators.Optional()])
    title = StringField('title', [validators.Optional()])
    date = StringField('date', [validators.Optional()])