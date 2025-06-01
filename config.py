# # # This file is used to store the config values of our flask app 

import os

from dotenv import load_dotenv

# configuring our base directory path 
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    # defining our SECRET_KEY in Config as ENVIRONMENT_VARIABLE
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # configuring our SQLALCHEMY_DATABASE_URI path to access our db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir,'app.db')

    # configuring the ERROR mailing 
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    ADMINS = ['nikhilsharma.csgeek@gmail.com']
    MAIL_DEFAULT_SENDER=('Nick Microblog test', 'nikhilsharma.csgeek@gmail.com')

    POSTS_PER_PAGE = 10

    # Supporting Languages for Translation 
    LANGUAGES = ['en', 'ja', 'hi', 'ar'] 

    # Translator Key (No Key) 
    TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')