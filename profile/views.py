from flask import render_template, Blueprint

bp = Blueprint('profile', __name__, template_folder='templates')


@bp.get("/profile")
def showProfile():
    return render_template('profile.html')
