from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    url = db.Column(db.String, unique = True, nullable = False)
    price = db.Column(db.String, nullable = False)
    image = db.Column(db.String, nullable = False)

    def __repr__(self):
        return '<Product {} {}>'.format(self.title, self.url)
