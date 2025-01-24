# importing the Flask class from flask package 
from flask import Flask
from config import Config

# creating the object of our application from Flask class, and providing the default __name__ configuration for current package which is __init.py__ 
app=Flask(__name__)


# We use a secret key for our wtf-forms to get protected against the CSRF attacks, so this configuration is important 
# app.config['SECRET_KEY']='you-will-never-guess'
app.config.from_object(Config)

# Using it to handle cyclic imports issue 
from flaskapp import routes