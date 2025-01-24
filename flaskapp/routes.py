# importing our app from flaskapp module 
from flaskapp import app
# using flask packages 
from flask import render_template, flash, redirect, url_for
# importing our LoginForm from flaskapp.forms package 
from flaskapp.forms import LoginForm


# our base route 
@app.route('/')
@app.route('/index')
def index():
    user = {"user":"Nikhil"}
    page_title = "Blog Application"
    user_posts=[
        {"author":"Nick","content":"Best Post so far on ReactJS"},
        {"author":"Jane","content":"Flask is the new future"},
        {"author":"Sierra","content":"Papaya is cool"},
    ]
    return render_template("index.html",user=user,title=page_title,posts=user_posts)


# loginpage route 
@app.route("/login",methods=['GET','POST'])
def login():
    loginform=LoginForm()
    if loginform.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(loginform.username.data, loginform.remember_me.data))
        redirect(url_for('index'))
    return render_template('login.html',title='Sign In',form=loginform)
