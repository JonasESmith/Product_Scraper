# Programmer : Jonas Smith
# Purpose    : Scrape the website given for my_url and produces items that are linked with the list

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pathlib import Path

import os
import json
import time
import codecs
import csv

csv_name = "joyOrganics.csv"

my_file = Path(csv_name)


storage = open(csv_name, 'w', newline='')
csvwriter = csv.writer(storage)

f = codecs.open("joyOrganics.html", "r")

page_html = f

# html parsing
page_soup = soup(page_html, "html.parser")

#gets all product items that are in a list element
products = page_soup.findAll("li", {"class": "tier"})

header = ["name", "address", "phone", "url"]
csvwriter.writerow(header)

for product in products : 
    name = product.find("h4", {"class" : "storemapper-title"}).text.strip()
    
    # this shouldn't happen but you never know
    if name == None : 
        name = "no name given"

    address = product.find("p", {"class": "storemapper-address"}).text.strip()

    if address == None:
        address = "no address given"

    phone = product.find("div")
    if phone != None :
        phone = phone.find("p")
        if phone != None:
            phone = phone.find("a").text.strip()

    if phone == None :
        phone = "no phone given"

    url = product.find("p", {"class", "storemapper-url"})

    if url != None :
        url = url.find("a")["href"]
    else :
        url = "no url given"

    fields = [name, address, phone, url]
    csvwriter.writerow(fields)

storage.close()

print("File created for CBDLifeCSV")