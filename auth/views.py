from flask import render_template, Blueprint
from auth.forms import RegisterForm, LoginForm

bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@bp.get("/login")
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@bp.get("/register")
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form=form)
