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
        return redirect(url_for('movies.showPopular'))
    cover_id = saveImage(request.files['cover'])
    banner_id = saveImage(request.files['banner'])
    title = payload.title.data
    description = payload.description.data
    date = payload.date.data
    directorFirstName = payload.directorFirstName.data
    directorLastName = payload.directorLastName.data
    director = Director.query.filter(Director.first_name == directorFirstName and Director.last_name == directorLastName).first()
    if not director:
        director = Director(directorFirstName, directorLastName)
        db.session.add(director)
        db.session.commit()
    movie = Movie(cover_id, banner_id, director.id, title, description, date)
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('movies.showPopular'))



@bp.post('/<int:id>')
def updateMovie(id):
    payload = UpdateMovieForm()
    if not payload.validate():
        return redirect(url_for('movies.showPopular'))
    movie = Movie.query.filter(Movie.id == id).first()
    if not movie:
        return redirect(url_for('movies.showPopular'))
    old_cover_id = None
    old_banner_id = None
    if payload.title.data:
        movie.title = payload.title.data
    if payload.description.data:
        movie.description = payload.description.data
    if payload.date.data:
        movie.date = payload.date.data
    if payload.directorFirstName.data and payload.directorLastName.data:
        directorFirstName = payload.directorFirstName.data
        directorLastName = payload.directorLastName.data
        director = Director.query.filter(Director.first_name == directorFirstName and Director.last_name == directorLastName).first()
        if not director:
            director = Director(directorFirstName, directorLastName)
            db.session.add(director)
            db.session.commit()
        movie.director_id = director.id
    if request.files['cover']:
        cover_id = saveImage(request.files['cover'])
        old_cover_id = movie.cover_id
        movie.cover_id = cover_id
    if request.files['banner']:
        banner_id = saveImage(request.files['banner'])
        old_banner_id = movie.banner_id
        movie.banner_id = banner_id
    db.session.add(movie)
    db.session.commit()
    if old_cover_id:
        Image.delete(old_cover_id)
    if old_banner_id:
        Image.delete(old_banner_id)
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
    return redirect(url_for('movies.showPopular'))



def saveImage(file):
    filename = secure_filename(file.filename)
    extension = filename.split('.')[-1]
    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16)) + "." + extension
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
    image = Image(file_name)
    db.session.add(image)
    db.session.flush()
    return image.id