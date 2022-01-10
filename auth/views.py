from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_user, login_required, logout_user

from app import db
from auth.forms import RegisterForm, LoginForm
from users.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@bp.get("/login")
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@bp.get("/register")
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form=form)


@bp.get('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('movies.showPopular'))


@bp.post('/login')
def loginSubmit():
    form = LoginForm()
    if not form.validate_on_submit():
        return redirect(url_for("auth.login"))
    user = User.query.filter_by(email=form.email.data).first()

    if not user or not user.check_password(form.password.data):
        return 'User does not exist message placeholder'
    login_user(user)
    return redirect(url_for("movies.showPopular"))


@bp.post('/register')
def registerSubmit():
    form = RegisterForm()
    if not form.validate_on_submit():
        return redirect(url_for("auth.register"))

    existingUser = User.query.filter_by(email=form.email.data).first()
    if existingUser:
        return 'User already exist message placeholder'

    user = User(form.email.data, form.password.data)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return redirect(url_for("movies.showPopular"))