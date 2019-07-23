from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# tthis gets products under $25 
my_url = 'https://420beast.com/collections/under-25?view=view-48&grid_list=list-view'

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
count = 1

for prod in products:
	try:
		prod_Name = prod.find("h2",{"class":"productitem--title"}).text.strip()
		prod_Vndr = prod.find("h3",{"class":"productitem--vendor"}).text.strip()
		prod_pric = prod.find("span",{"class":"money"}).text.strip()
		prod_dsct = prod.find("div",{"class":"productitem--description"}).text.strip()


		print(str(count) + " ")
		print("Product Name        : " + prod_Name)
		print("Product Vendor      : " + prod_Vndr)
		print("Product Price       : " + prod_pric)
		print("Product Description : " + prod_dsct)	
		print()
		count = count + 1
	except :
		print(str(count) + " ")
		print("Something went wrong")
		count = count + 1