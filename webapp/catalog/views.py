from flask import Blueprint, current_app, render_template

from webapp.catalog.models import Catalog

blueprint = Blueprint('catalog', __name__)

@blueprint.route('/')
def index():
    title = "Смарт-часы"
    catalog = Catalog.query.all()
    return render_template('catalog/index.html', catalog = catalog, page_title = title)
