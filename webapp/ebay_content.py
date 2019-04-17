import requests
from bs4 import BeautifulSoup

from webapp.db import db
from webapp.catalog.models import Catalog

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text

    except(requests.RequestException, ValueError):
        return False

def get_ebay_products():
    html = get_html("https://ru.ebay.com/b/Smart-Watches/178893/bn_152365")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_products = soup.find('ul', class_='b-list__items_nofooter').findAll('li')
        products_list = []
        for product in all_products:
            title = product.find('h3').text
            url = product.find('a')['href']
            price = product.find('div', 's-item__detail s-item__detail--primary').text
            try:
                image = product.find('img')['data-src']
            except KeyError:
                image = product.find('img')['src']
            save_catalog(title, url, price, image)

def save_catalog(title, url, price, image):
    catalog_exists = Catalog.query.filter(Catalog.url == url).count()
    print(catalog_exists)
    if not catalog_exists:
        catalog_item = Catalog(title = title, url = url, price = price, image = image)
        db.session.add(catalog_item)
        db.session.commit()
