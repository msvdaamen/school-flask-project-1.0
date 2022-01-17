import os
import string
import random

from flask import render_template, Blueprint
from werkzeug.utils import secure_filename

from app import ALLOWED_EXTENSIONS, app
from movies.forms import UpdateMovieForm
from movies.models.movie import Movie

bp = Blueprint('movies', __name__, url_prefix='/movies', template_folder='templates')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.get("/popular")
def showPopular():
    movies = Movie.query.join(Movie.cover).all()
    return render_template('popular.html', movies=movies)


@bp.get('/<int:id>')
def getMovie(id):
    movie = Movie.query.filter(Movie.id == id).first()
    return movie.toJson()


@bp.post('<int:id>')
def updateMovie(id):
    payload = UpdateMovieForm()
    if not payload.validate():
        return "Bad request", 400
    cover = payload.cover.data
    if cover:
        filename = secure_filename(cover.filename)
        extension = filename.split('.')[-1]
        file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16)) + "." + extension
        cover.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        return file_name
    return {
        "hier": "adasd"
    }