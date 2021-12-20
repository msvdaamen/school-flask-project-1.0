from flask import render_template, Blueprint
from auth.forms import RegisterForm, LoginForm

bp = Blueprint('movies', __name__, url_prefix='/movies', template_folder='templates')

@bp.get("/popular")
def showPopular():
    return render_template('popular.html')
