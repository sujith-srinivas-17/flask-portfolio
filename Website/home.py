from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def homepage():
    return render_template("home.html")  # Render home.html instead of base.html