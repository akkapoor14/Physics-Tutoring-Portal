# this file contains information about what configuration we want to
# run our server with, based off of the env

# using example from here:
# https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

import os


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class LocalConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
