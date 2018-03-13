from flask import Blueprint, render_template, request, redirect, url_for, flash
from project.models import User
from project import db
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import IntegrityError
from functools import wraps

users_blueprint = Blueprint('users', __name__, template_folder='templates')


def ensure_admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.is_admin:
            return redirect(url_for('root'))
        return fn(*args, **kwargs)

    return wrapper


@users_blueprint.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        found_user = User.authenticate(request.form['email'],
                                       request.form['password'])
        if found_user:
            login_user(found_user)
            return redirect(url_for('users.account'))
        flash("Invalid credentials")
    return render_template("login.html")


@users_blueprint.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        try:
            new_user = User(**dict(request.form.items()))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
        except IntegrityError as e:
            flash("Email already taken")
            return render_template('signup.html')
        return redirect(url_for('users.account'))
    return render_template("signup.html")


@users_blueprint.route('/account')
@login_required
def account():
    return render_template("account.html")


@users_blueprint.route('/admin')
@login_required
@ensure_admin
def admin():
    return render_template("admin.html", users=User.query.all())


@users_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('root'))