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


ourFileName = "top_shelf_hemp"

my_url = "https://www.topshelfhemp.co/map?fbclid=IwAR3D6NX3b4E_uhZ3hRvq526yRXvfJprI3cMyMPFl-1r758oDcddjw52a9HE_aem_AV03lU6wZWa1nJPb1WqcJN9Unq-Si5IOoKEKs7pFKIzXdhapQ39S9b7m4b3vQKjIQCk"
csv_name = ourFileName + ".csv"

# opens connection and retrieves page
uClient = uReq(my_url)

my_file = Path(csv_name)


storage = open(csv_name, "w", newline="")
csvwriter = csv.writer(storage)

# outputs page into variable
# page_html = uClient.read()

f = codecs.open(ourFileName + ".html", "r")

# outputs page into variable
# page_html = uClient.read()

page_html = f

# print("Opened connection to " + my_url)

# print(page_html)

# closes connection
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# gets all product items that are in a list element
products = page_soup.findAll(
    "div",
    {
        "class": "maplibregl-marker mapboxgl-marker maplibregl-marker-anchor-center mapboxgl-marker-anchor-center located-marker"
    },
)

print("There are " + str(len(products)) + " locations")

header = ["name", "address"]
csvwriter.writerow(header)

for store in products:
    #  print the title of the store
    print(store["title"])
    name = store["title"]

    # this shouldn't happen but you never know
    if name == None:
        name = "no name given"

    fields = [name]
    csvwriter.writerow(fields)


storage.close()

print("File created for " + ourFileName)
