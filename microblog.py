# starting app from here 
from flaskapp import app

import sqlalchemy as sa
import sqlalchemy.orm as so
from flaskapp import app, db, cli
from flaskapp.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}