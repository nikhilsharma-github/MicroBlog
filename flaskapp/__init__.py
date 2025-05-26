# importing the Flask class from flask package 
from flask import Flask
# importing the Config Class from config.py package 
from config import Config
# importing SQLAlchemy class from flask_sqlalchemy package 
from flask_sqlalchemy import SQLAlchemy 
# importing Migrate Class from flask_migrate package 
from flask_migrate import Migrate 
# importing LoginManager Class from flask-login package for utilizing Login Functionalities 
from flask_login import LoginManager
# importing logging package for event logging 
import logging 
# sends SMPT email for each logging event 
# file application logger 
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail



# creating the object of our application from Flask class, and providing the default __name__ configuration for current package which is __init.py__ 
app=Flask(__name__)


# We use a secret key for our wtf-forms to get protected against the CSRF attacks, so this configuration is important 
# app.config['SECRET_KEY']='you-will-never-guess'
app.config.from_object(Config)

# creating the object for Flask Mail Service 
mail = Mail(app)

# providing our app to the SQLAlchemy class to get the db object, this object represents our database
db=SQLAlchemy(app)
# providing our app and the db to the Migrate class to get the migrate object, this migrate object represents our database migration engine

migrate=Migrate(app,db)

# creating a login object from the LoginManager Class which will take care of the Login related logics and redirections 
login=LoginManager(app)
login.login_view='login'

# Using it to handle cyclic imports issue 
# this model package will define the structure of our database 
# routes define the routing of our application 


# Error Hadling using Event Logging(By Mail):
if not app.debug:
    # Email Logger 
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    # File Logger 
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                        backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')


from flaskapp import routes, models, errors