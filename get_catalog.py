from webapp import create_app
from webapp.ebay_content import get_ebay_snippets, get_ebay_content

app = create_app()
with app.app_context():
    get_ebay_snippets()
    get_ebay_content()