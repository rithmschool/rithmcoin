from project import db, bcrypt
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    coins = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean, default=False)
    transactions = db.relationship(
        'Transaction',
        primaryjoin="or_(User.id==Transaction.sender_id, "
        "User.id==Transaction.recipient_id)")

    def __init__(self, name, email, password, is_admin=False):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.is_admin = is_admin
        self.coins = 1000

    @classmethod
    def authenticate(cls, email, password):
        found_user = cls.query.filter_by(email=email).first()
        if found_user:
            authenticated_user = bcrypt.check_password_hash(
                found_user.password, password)
            if authenticated_user:
                return found_user
        return False


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column('sender_id', db.Integer, db.ForeignKey('users.id'))
    recipient_id = db.Column('recipient_id', db.Integer,
                             db.ForeignKey('users.id'))
    amount = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)
    sender = db.relationship('User', foreign_keys=[sender_id])
    recipient = db.relationship('User', foreign_keys=[recipient_id])

    def __init__(self, sender_id, recipient_id, amount):
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.amount = amount
