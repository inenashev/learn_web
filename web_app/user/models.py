from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from web_app.db import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def __repr__(self):
        return f'<User {self.username}, id {self.id}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'