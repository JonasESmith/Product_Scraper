from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

my_strings = [
	'under-25',
	'25-50',
	'50-100',
	'over-100',
]

my_page_count = [
	7,
	13,
	10,
	4,
]

my_urls = [ ]

# simple count variable to show number of products
index = 0
count = 1

class Product:
	def __init__(self ,name, vendor, price, description):
		self.name = name
		self.vendor = vendor
		self.price = price
		self.description = description

product_list = []


for iterator in my_page_count:

	my_urls = []

	for x in range(iterator):
		value = 'https://420beast.com/collections/{}?page={}&view=view-48&grid_list=list-view'.format(my_strings[index], str(x))

		my_urls.append(value)

	for link in my_urls:
		# this sets the my_url variable to the link passed by my_urls...
		# I could probably use a better naming scheme
		my_url = link

		# opens connection and retreives page
		uClient = uReq(my_url)

		# outputs page into variable
		page_html = uClient.read()

		# closes connection
		uClient.close()

		# html parsing
		page_soup = soup(page_html, "html.parser")

		# will get the div elements that were returned! how neat is that
		page_soup.div

		#gets all product items that are in a list element
		products = page_soup.findAll("div", {"class":"productitem"})
		len(products)

		for prod in products:
			try:
				prod_Name = prod.find("h2",{"class":"productitem--title"}).text.strip()
				prod_Vndr = prod.find("h3",{"class":"productitem--vendor"}).text.strip()
				prod_pric = prod.find("span",{"class":"money"}).text.strip()
				prod_dsct = prod.find("div",{"class":"productitem--description"}).text.strip()

				tmpProd = Product(prod_Name, prod_Vndr, prod_pric, prod_dsct)
				
				count = count + 1

				product_list.append(tmpProd)
			except :
				print(str(count) + " ")
				print("Something went wrong")
				count = count + 1

	index = index + 1

for x in product_list:
	print(x)

print(len(product_list))

def obj_dict(obj):
    return obj.__dict__

json_string = json.dumps(product_list, default=obj_dict)

print(json_string)