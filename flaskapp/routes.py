# importing our app from flaskapp module 
from flaskapp import app
# using flask packages 
from flask import render_template, flash, redirect, url_for, request
from urllib.parse import urlsplit
# importing our Form from flaskapp.forms package 
from flaskapp.forms import LoginForm, RegistrationForm, EditProfileForm
# methods to check for current user and logged in user 
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from flaskapp import db
from flaskapp.models import User
from datetime import datetime, timezone

# This decorator will execute before the view function 
# Updating the last seen value for the user whenever user logs in 
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()

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


# User Profile Route 
@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts=[
        {"author": user, 'body':"Test Post #1"},
        {"author": user, 'body':"Test Post #2"}
    ]
    return render_template('user.html',user=user,posts=posts)

# User Profile Edit Route 
@app.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Profile Updated Successfully')
        return redirect(url_for("edit_profile"))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html',title="Edit Profile",form=form)

