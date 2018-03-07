from flask import Blueprint, render_template, request
from project.models import User
from project import db

users_blueprint = Blueprint('users', __name__, template_folder = 'templates')

@users_blueprint.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
    return render_template("login.html")

@users_blueprint.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        pass
    return render_template("signup.html")

@users_blueprint.route('/logout')
def logout():
    pass

@users_blueprint.route('/account')
def account():
    pass