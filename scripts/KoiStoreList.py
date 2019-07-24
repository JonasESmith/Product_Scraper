from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import json
import re

class Store:
	def __init__(self ,name, address):
		self.name = name
		self.address = address

store_list = []

req = Request("https://www.bullseyelocations.com/pages/koi?f=2&radius=200", headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
stores = page_soup.findAll("div", {"class":"resultsDetails"})

for store in stores:
    name = store.h3.text.strip()
    address = store.address.text.strip()

    store = Store(name, address)
    store_list.append(store)

index = 1

for x in store_list:
    print(index)
    print(x.name)
    print(x.address)
    print()
    index = index + 1