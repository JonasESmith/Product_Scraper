from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import json
import re
import pickle

class Product:
	def __init__(self ,name, alt, price, link):
		self.name = name
		self.alt = alt
		self.price = price
		self.link = link
	def addJson(self, jsonVal):
		self.jsonVal = jsonVal

product_list = []

my_strings = [
	'koi-cbd-naturals-oil',
	'koi-cbd-gummies',
	'koi-cbd-vape-oil',
	'koi-cbd-vape-devices-carts',
    'koi-cbd-topicals',
    'koi-cbd-pets',
    #'koi-cbd-merchandise'
]

# re-init blank my_urls list in order to iterate through and "grab" products
my_urls = []

for link in my_strings:
    # this potentially could be user input
    value = 'https://koicbd.com/{}'.format(link)
    # simply adds the url formatted into the my_urls list
    my_urls.append(value)

for link in my_urls:
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    products = page_soup.findAll("li", {"class": "product"})

    for prod in products:
        name = prod.find("h2", {"class":"woocommerce-loop-product__title"}).text.strip()
        alt = prod.find("img", {"class":"attachment-woocommerce_thumbnail"})["alt"]
        price = prod.find("span", {"class", "price"}).text.strip()
        link = prod.find("a", {"class":"woocommerce-LoopProduct-link"})["href"]

        product = Product(name, alt, price, link)

        product_list.append(product)

actual_list = []

for x in product_list:
    count = 0
    for y in actual_list:
        if(x.name == y.name):
            count = count + 1
    if(count == 0):
        actual_list.append(x)

for prod in actual_list:
    req = Request(prod.link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    scripts = page_soup.findAll('script', {"src": False})

    newLine = ""

    for script in scripts:
        for line in script:
            if(line is not None):
                if ("tvc_po=" in line):
                    newLine = line

    newLine = newLine.split("\n")
    for line in newLine:
        if("tvc_po=" in line):
            newline = line.replace("tvc_po=","").replace(";","")
            break

    # json_values = json.dumps(newline)
    # # json_dump_values = json.dumps(json_values, indent=4, sort_keys=True)

    prod.addJson(newline)

for x in actual_list:
    print(x.name)
    print(x.jsonVal)
    print()

def obj_dict(obj):
    return obj.__dict__

# converst the object list to json
json_string = json.dumps(actual_list, default=obj_dict)

text_file = open("KoiCBD.json", "w")
text_file.write(json_string)
text_file.close()

print()
print("end")