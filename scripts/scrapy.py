from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# this currently just gets my github repo page
my_url = 'https://github.com/JonasESmith?tab=repositories'

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
repos = page_soup.findAll("li",{"class":"col-12"})

len(repos)
count = 1;

for repo in repos:
	try:
		repo_title = repo.div.div.h3.a.text.strip()
		repo_dscpt = repo.div.p.text.strip()

		# gets the language
		span_langu = repo.findAll("span",{"itemprop":"programmingLanguage"})
		repo_langu = span_langu[0].text
		print(str(count) + " ")
		print("title       : " + repo_title)
		print("description : " + repo_dscpt)
		print("language    : " + repo_langu)
		print()
		count = count + 1
	except :
		print(str(count) + " ")
		print("Something went wrong")
		count = count + 1