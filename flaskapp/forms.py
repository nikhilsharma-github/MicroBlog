# import FlaskForm Class 
from flask_wtf import FlaskForm
# importing elements for our form 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
# importing DataValidation element 
from wtforms.validators import DataRequired


# creating a class for our LoginForm and its objects 
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')