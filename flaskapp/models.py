from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from flaskapp import db
from flaskapp import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flaskapp import login
# gives MD5 hash which is cryptographic in nature 
from hashlib import md5


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                            unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(
        back_populates='author')
    # to store user's about me information 
    about_me: so.Mapped[Optional[str]] = so.mapped_column(sa.String(140))
    # to store last seen time of user 
    last_seen: so.Mapped[Optional[datetime]] = so.mapped_column(default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    # set hashed password method
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    # check hashed password method 
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    # create avatar class 
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=monsterid&s={size}'

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),
                                                index=True)

    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
# a method to check for the user id for keeping track of the logged in user by storing its unique identifier 
@login.user_loader
def load_user(id):
    return db.session.get(User,int(id))