from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, EmailField, FileField

class CreateMovieForm(FlaskForm):
    cover = FileField('cover', [validators.DataRequired()])
    banner = FileField('banner', [validators.DataRequired()])
    title = StringField('title', [validators.DataRequired()])
    description = StringField('description', [validators.DataRequired()])
    date = StringField('date', [validators.DataRequired()])
    directorFirstName = StringField('directorFirstName', [validators.DataRequired()])
    directorLastName = StringField('directorLastName', [validators.DataRequired()])


class UpdateMovieForm(FlaskForm):
    cover = FileField('cover', [validators.Optional()])
    banner = FileField('banner', [validators.Optional()])
    title = StringField('title', [validators.Optional()])
    description = StringField('description', [validators.Optional()])
    date = StringField('date', [validators.Optional()])
    directorFirstName = StringField('directorFirstName', [validators.Optional()])
    directorLastName = StringField('directorLastName', [validators.Optional()])