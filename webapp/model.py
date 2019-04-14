from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    url = db.Column(db.String, unique = True, nullable = False)
    price = db.Column(db.String, nullable = False)
    image = db.Column(db.String, nullable = False)

    def __repr__(self):
        return '<Product {} {}>'.format(self.title, self.url)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(45), index = True, unique = True)
    password = db.Column(db.String(120))
    role = db.Column(db.String(10), index = True)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User name={} id={}>'.format(self.username, self.id)
