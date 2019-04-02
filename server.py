from flask import Flask, render_template

from ebay_content import get_ebay_products

app = Flask(__name__)

@app.route('/')
def index():
    catalog = get_ebay_products()
    return render_template('index.html', catalog = catalog)

if __name__ == "__main__":
    app.run(debug=True)