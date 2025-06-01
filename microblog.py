# starting app from here 

import sqlalchemy as sa
import sqlalchemy.orm as so
from flaskapp import create_app, db
from flaskapp.models import User, Post

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}