import requests
from bs4 import BeautifulSoup

from webapp.db import db
from webapp.catalog.models import Catalog

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
    }
    try:
        result = requests.get(url, headers = headers)
        result.raise_for_status()
        return result.text

    except(requests.RequestException, ValueError):
        return False

def get_ebay_snippets():
    html = get_html("https://www.ebay.com/sch/i.html?_from=R40&_nkw=&_sacat=178893&_sop=12")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_products = soup.find('ul', class_='srp-results srp-list clearfix').findAll('li', class_='s-item')
        for product in all_products:
            title = product.find('h3', class_='s-item__title').text
            url = product.find('a', class_='s-item__link')['href']
            price = product.find('span', class_='s-item__price').text
            image = product.find('img', class_='s-item__image-img')['src']
            save_catalog(title, url, price, image)

def save_catalog(title, url, price, image):
    catalog_exists = Catalog.query.filter(Catalog.url == url).count()
    print(catalog_exists)
    if not catalog_exists:
        catalog_item = Catalog(title = title, url = url, price = price, image = image)
        db.session.add(catalog_item)
        db.session.commit()

def get_ebay_content():
    catalog_without_text = Catalog.query.filter(Catalog.text.is_(None))
    for catalog in catalog_without_text:
        html = get_html(catalog.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            catalog_text = soup.find('div', class_='iti-eu-txt').decode_contents()
            if catalog_text:
                catalog.text = catalog_text
                db.session.add(catalog)
                db.session.commit()
