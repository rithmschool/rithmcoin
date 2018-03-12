import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)

import os

if os.environ.get('ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

from project.users.views import users_blueprint
from project.transactions.views import transactions_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(transactions_blueprint, url_prefix='/transactions')

login_manager.login_view = "users.login"

from project.models import User


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def root():
    return render_template("home.html")