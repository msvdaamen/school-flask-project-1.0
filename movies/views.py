from flask import render_template, Blueprint, jsonify
from itsdangerous import Serializer

from movies.models.movie import Movie

bp = Blueprint('movies', __name__, url_prefix='/movies', template_folder='templates')

@bp.get("/popular")
def showPopular():
    movies = Movie.query.all()
    return render_template('popular.html', movies=movies)


@bp.get('/<int:id>')
def getMovie(id):
    movie = Movie.query.filter(Movie.id == id).first()
    return movie.toJson()