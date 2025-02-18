# importing our app from flaskapp module 
from flaskapp import app
# using flask packages 
from flask import render_template, flash, redirect, url_for, request
from urllib.parse import urlsplit
# importing our LoginForm from flaskapp.forms package 
from flaskapp.forms import LoginForm, RegistrationForm
# methods to check for current user and logged in user 
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from flaskapp import db
from flaskapp.models import User


# our base route 
@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {"user":"Nikhil"}
    page_title = "Blog Application"
    user_posts=[
        {"author":"Nick","content":"Best Post so far on ReactJS"},
        {"author":"Jane","content":"Flask is the new future"},
        {"author":"Sierra","content":"Papaya is cool"},
    ]
    return render_template("index.html",title='Homepage',posts=user_posts)


# loginpage route 
@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for(index))
    
    loginform=LoginForm()
    if loginform.validate_on_submit():
        user  = db.session.scalar(
            sa.select(User).where(User.username==loginform.username.data)
        )
        if user is None or not user.check_password(loginform.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user,remember=loginform.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page =  url_for('index')
        return redirect(next_page)
    return render_template('login.html',title="Sign In",form=loginform)

# logout route 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


# Register Page Route  
@app.route('/Register',methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    registrationform = RegistrationForm()
    if registrationform.validate_on_submit():
        user = User(username=registrationform.username.data, email=registrationform.email.data)
        user.set_password(registrationform.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=registrationform)
