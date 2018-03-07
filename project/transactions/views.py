from flask import Blueprint, render_template, request, redirect, url_for, flash
from project.models import User
from project import db
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import IntegrityError

transactions_blueprint = Blueprint('transactions', __name__)

@transactions.route('', methods=["POST"])
@login_required
def create():
    from IPython import embed; embed()
    return redirect(url_for("users.account"))
