from flask import Flask, render_template

from webapp.model import db, Catalog

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        catalog = Catalog.query.all()
        return render_template('index.html', catalog = catalog)
    
    return app

