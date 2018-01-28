# Using beautifulsoup for web scrapping
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

## test
# try reading github file
url = "https://raw.githubusercontent.com/ys3006/Art-parser/master/data/2015-03-18/lot1.html"

# open the html, grabbing the page
uOpen = uReq(url)
page_html = uOpen.read()
# close the connection
uOpen.close()
