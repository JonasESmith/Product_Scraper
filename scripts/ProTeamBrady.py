from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
import time

my_strings = [
	129,
	81,
	90,
	73,
    106,
    116,
    76,
    148,
    105,
    120
]

my_page_count = [
	2,
	2,
	2,
	5,
    3,
	2,
	2,
	2,
    2,
    1,
]

# simple count variable to show number of products
index = 0
count = 1

# very simple product class
class Product:
	def __init__(self ,name, price, description):
		self.name = name
		self.price = price
		self.description = description

product_list = []

# simple time reporting tool
start_time = time.time()
for iterator in my_page_count:

	# re-init blank my_urls list in order to iterate through and "grab" products
	my_urls = []

	for x in range(iterator):
		# this potentially could be user input
		value = 'https://proteambrady.com/hemp-cbd-products/?_bc_fsnf=1&brand={}&sort=newest&page={}'.format(my_strings[index], str(x))
		# simply adds the url formatted into the my_urls list
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

		#gets all product items that are in a list element
		products = page_soup.findAll("article", {"class":"product-item-container"})

		for prod in products:
			# tries to create a new simple product object and adds to list of products
			try:
				prod_Name = prod.find("h4",{"class":"card-title"}).a.text.strip()
				prod_pric = prod.find("span",{"class":"price--withoutTax"}).text.strip()
				prod_dsct = prod.find("div",{"class":"description"}).text.strip()

				tmpProd = Product(prod_Name, prod_pric, prod_dsct)

				count = count + 1

				product_list.append(tmpProd)
			except :
				print(str(count) + " ")
				print("Something went wrong")
				count = count + 1

	index = index + 1

print("This task completed in " + str( time.time() - start_time ) + " seconds" )

# the reference I used to serialize the obj_list to json
# https://stackoverflow.com/questions/26033239/list-of-objects-to-json-with-python
def obj_dict(obj):
    return obj.__dict__

# converst the object list to json
json_string = json.dumps(product_list, default=obj_dict)

# writes the json string to a file stored locally
text_file = open("ProTeamBrady.json", "w")
text_file.write(json_string)
text_file.close()

# final report to user when script is ran
print("Pulled " + str(len(product_list)) + " products from ProTeamBrady.com, and saved them to ProTeamBrady.json!")
print("This task completed in " + str( time.time() - start_time ) + " seconds" )

print(len(product_list))