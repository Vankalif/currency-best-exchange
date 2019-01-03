# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
# from app import Config

r = requests.get('https://www.banki.ru/products/currency/cb/')
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
