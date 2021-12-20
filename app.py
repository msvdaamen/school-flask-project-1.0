from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route("/auth/login")
def hello_world():
    return render_template('auth/login.html')


@app.route("/auth/register")
def hello_world():
    return render_template('auth/register.html')
