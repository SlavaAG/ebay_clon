from webapp import create_app
from webapp.ebay_content import get_ebay_products

app = create_app()
with app.app_context():
    get_ebay_products()