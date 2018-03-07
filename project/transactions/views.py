from flask import Blueprint, request, redirect, url_for, flash
from project.models import User, Transaction
from project import db
from flask_login import current_user, login_required

transactions_blueprint = Blueprint('transactions', __name__)

@transactions_blueprint.route('', methods=["POST"])
@login_required
def create():
    amount = min(current_user.coins, int(request.form['amount']))
    recipient = User.query.filter_by(email = request.form['email']).first()
    if recipient and amount > 0:
        new_transaction = Transaction(current_user.id,
                                      recipient.id,
                                      amount)
        current_user.coins -= amount
        recipient.coins += amount
        db.session.add_all([current_user, recipient, new_transaction])
        db.session.commit()
    else:
        flash("Invalid form data.")
    return redirect(url_for("users.account"))
