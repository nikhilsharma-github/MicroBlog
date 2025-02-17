# importing the Flask class from flask package 
from flask import Flask
# importing the Config Class from config.py package 
from config import Config
# importing SQLAlchemy class from flask_sqlalchemy package 
from flask_sqlalchemy import SQLAlchemy 
# importing Migrate Class from flask_migrate package 
from flask_migrate import Migrate 


# creating the object of our application from Flask class, and providing the default __name__ configuration for current package which is __init.py__ 
app=Flask(__name__)


# We use a secret key for our wtf-forms to get protected against the CSRF attacks, so this configuration is important 
# app.config['SECRET_KEY']='you-will-never-guess'
app.config.from_object(Config)

# providing our app to the SQLAlchemy class to get the db object, this object represents our database
db=SQLAlchemy(app)
# providing our app and the db to the Migrate class to get the migrate object, this migrate object represents our database migration engine

migrate=Migrate(app,db)

# Using it to handle cyclic imports issue 
# this model package will define the structure of our database 
# routes define the routing of our application 
from flaskapp import routes, models