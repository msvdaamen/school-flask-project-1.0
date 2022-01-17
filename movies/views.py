import os
import string
import random

from flask import render_template, Blueprint, url_for, request
from sqlalchemy.orm import aliased
from werkzeug.utils import secure_filename, redirect

from app import ALLOWED_EXTENSIONS, app, db
from directors.models.director import Director
from images.models.Image import Image
from movies.forms import UpdateMovieForm, CreateMovieForm
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
    cover = aliased(Image)
    banner = aliased(Image)
    movie = Movie.query.join(cover, Movie.cover).join(banner, Movie.banner).filter(Movie.id == id).first()
    return movie.toJson()


@bp.post('')
def createMovie():
    payload = CreateMovieForm()
    if not payload.validate():
        return "Bad request", 400
    cover_id = saveImage(request.files['cover'])
    banner_id = saveImage(request.files['banner'])
    title = payload.title.data
    date = payload.date.data
    tempName = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    insertDirector = Director("Temp", tempName)
    db.session.add(insertDirector)
    db.session.commit()
    movie = Movie(cover_id, banner_id, insertDirector.id, title, date)
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('movies.showPopular'))



# @bp.post('<int:id d):
    # payload = UpdateMovieForm()
    # if not payload.validate():
    #     return "Bad request", 400
    # cover = payload.cover.data
    # if cover:
    #     filename = secure_filename(cover.filename)
    #     extension = filename.split('.')[-1]
    #     file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16)) + "." + extension
    #     cover.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
    # return {
    #     "hier": "adasd"
    # }



def saveImage(file):
    filename = secure_filename(file.filename)
    extension = filename.split('.')[-1]
    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16)) + "." + extension
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
    image = Image(file_name)
    db.session.add(image)
    db.session.flush()
    return image.id