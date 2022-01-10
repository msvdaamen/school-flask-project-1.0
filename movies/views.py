from flask import render_template, Blueprint

from movies.models.movie import Movie

bp = Blueprint('movies', __name__, url_prefix='/movies', template_folder='templates')

@bp.get("/popular")
def showPopular():
    movies = Movie.query.all()
    return render_template('popular.html', movies=movies)
