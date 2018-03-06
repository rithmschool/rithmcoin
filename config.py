import os

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost/rithmcoin'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevelopmentConfig(Config):
    DEBUG = True
