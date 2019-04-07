from flask import Flask, render_template

from webapp.ebay_content import get_ebay_products

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        catalog = get_ebay_products()
        return render_template('index.html', catalog = catalog)
    
    return app

