# import FlaskForm Class 
from flask_wtf import FlaskForm
from flask_babel import _, lazy_gettext as _l
# importing elements for our form 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
# importing DataValidation element 
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from flaskapp import db
from flaskapp.models import User


# creating a class for our LoginForm and its objects 
class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))

# creating a class for our RegistrationForm and its objects 
class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField( _l('Repeat Password'), validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self,username):
        user = db.session.scalar(sa.select(User).where(
            User.username==username.data
        ))
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self,email):
        user = db.session.scalar(sa.select(User).where(
            User.email==email.data
        ))
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))
        

# Reset Password Request Form 
class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))

# Reset Password Form 
class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(_l('Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))
            
# Empty Form for Submit Button 
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')