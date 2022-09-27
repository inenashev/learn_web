from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,nullable=False)
    url = db.Column(db.String,unique=True,nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.String,nullable=True)

    def __repr__(self):
        return f'News {self.title} {self.url}'


