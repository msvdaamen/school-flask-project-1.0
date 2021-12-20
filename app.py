from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route("/auth/login")
def login():
    return render_template('auth/login.html')


@app.route("/auth/register")
def register():
    return render_template('auth/register.html')
