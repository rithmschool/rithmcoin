from flask import Blueprint, abort
from project.models import User
from project import db

users_blueprint = Blueprint('users', __name__, template_folder = 'templates')

@users_blueprint.route('/login', methods=["GET", "POST"])
def login():
    pass

@users_blueprint.route('/signup', methods=["GET", "POST"])
def signup():
    pass

@users_blueprint.route('/logout')
def logout():
    pass

@users_blueprint.route('/account')
def account():
    pass