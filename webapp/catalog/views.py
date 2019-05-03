from flask import abort, Blueprint, current_app, render_template

from webapp.catalog.models import Catalog

blueprint = Blueprint('catalog', __name__)

@blueprint.route('/')
def index():
    title = "Смарт-часы"
    catalog = Catalog.query.filter(Catalog.text.isnot(None)).all()
    return render_template('catalog/index.html', catalog = catalog, page_title = title)

@blueprint.route('/catalog/<int:catalog_id>')
def product(catalog_id):
    my_product = Catalog.query.filter(Catalog.id == catalog_id).first()
    if not my_product:
        abort(404)
    return render_template('catalog/product.html', page_title = my_product.title, product = my_product)
