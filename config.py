# # # This file is used to store the config values of our flask app 

import os

# configuring our base directory path 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # defining our SECRET_KEY in Config as ENVIRONMENT_VARIABLE
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # configuring our SQLALCHEMY_DATABASE_URI path to access our db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir,'app.db')