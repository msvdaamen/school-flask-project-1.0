from flask import Flask, redirect, send_from_directory
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_file("config.json", load=json.load)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/movie-project?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'public/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/public/images/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.root_path + '/public/images/', filename)

from auth.views import bp as AuthBlueprint
from movies.views import bp as MoviesBlueprint
from profile.views import bp as ProfileBlueprint

app.register_blueprint(AuthBlueprint)
app.register_blueprint(MoviesBlueprint)
app.register_blueprint(ProfileBlueprint)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

from users.user import User
from directors.models.director import Director
from actors.models.actor import Actor
from movies.models.movie import Movie
from movies.models.movieRole import MovieRole
from images.models.Image import Image

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route("/")
def home():
    return redirect('/movies/recent-added')