from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup



req = Request('https://koicbd.com/koi-cbd-naturals-oil/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
products = page_soup.findAll("li", {"class": "product"})

for prod in products:
    name = prod.find("h2", {"class":"woocommerce-loop-product__title"}).text.strip()
    print(name)