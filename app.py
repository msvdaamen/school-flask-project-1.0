from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/movie-project?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from auth.views import bp as AuthBlueprint
from movies.views import bp as MoviesBlueprint

app.register_blueprint(AuthBlueprint)
app.register_blueprint(MoviesBlueprint)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

from users.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
