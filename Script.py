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

# html parser
page_soup = soup(page_html, 'html.parser')
# grab author name
page_soup.findAll('h2')[0].text


## Task 1 - artist + works
import glob

artist_container = []
works_container = []
price_container = []
for filename in glob.glob('/Users/Yifan/Downloads/lot-parser/data/2015-03-18/*.html'):
    page_soup = soup(open(filename, "r").read(), 'html5lib')
    containers = page_soup.findAll('body')
    
    for container in containers:
        artist = container.findAll('h2')[0]
        artist_container.append(artist.text)
        
        work = container.findAll('h3')[0]
        works_container.append(work.text)
        
        price = container.findAll('div')[1]
        price_container.append(price.text)

print(artist_container)
print(works_container)
print(price_container)

## Output - artist + works
# print output for 2015-03-18 directory
print('[')
for artist, works in zip(artist_container, works_container):
    out = ('  {' + '\n' 
           + '    artist: ' + "'" + artist + "'" + ', ' + '\n' 
           + '    works: [' + works + "']," + '\n'
           +'  },' + '\n')
    print(out)
print(']')

## Output - artist + works ＋ price
# print output for 2015-03-18 directory
print('[')
for artist, works, price in zip(artist_container, works_container, price_container):
    out = ('  {' + '\n' 
           + '    artist: ' + "'" + artist + "'" + ', ' + '\n' 
           + '    works: ' + '[' + '\n'
           + '    { ' + "title: '" + works + "', price: '" + price + "' }," + '\n'
           +'  },' + '\n')
    print(out)
print(']')

