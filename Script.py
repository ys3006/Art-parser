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


# separate currency and amount from pirce container
sep = []
for word in price_container:
    line = word.split(' ')
    sep.append(line)
print(sep)


# store currency and amount in two lists: currency_container and price_container2
currency_container = []
price_container2 = []

for item in sep:
    curr = item[0]
    num = item[1]
    currency_container.append(curr)
    price_container2.append(num)
    
print(currency_container)
print(price_container2)

## Output - artist + works ＋ currency + price amount
# print output for 2015-03-18 directory
print('[')
for artist, works, currency, price in zip(artist_container, works_container, currency_container, price_container2):
    out = ('  {' + '\n' 
           + '    artist: ' + "'" + artist + "'" + ', ' + '\n' 
           + '    works: ' + '[' + '\n'
           + '    { ' + "title: '" + works + "', currency: '" + currency + "', amount: '" + price + "' }," + '\n'
           +'  },' + '\n')
    print(out)
print(']')

#------ Task 1~4: 20 min ------#

## Task 5 - Grab from 2017-12-20 directory
artist2_container = []
works2_container = []
currency2_container = []
price2_container = []
for filename in glob.glob('/Users/Yifan/Downloads/lot-parser/data/2017-12-20/*.html'):
    page_soup = soup(open(filename, "r").read(), 'html5lib')
    
    for container in containers:
        artist = page_soup.findAll('h3', {'class': 'artist'})[0]
        artist2_container.append(artist.text)
        
        work = page_soup.findAll('h3')[1]
        works2_container.append(work.text)
        
        currency = page_soup.findAll('span', {'class': 'currency'})[0]
        currency2_container.append(currency.text)
        
        price = page_soup.findAll('span')[1]
        price2_container.append(price.text)
        
print(artist2_container)
print(works2_container)
print(currency2_container)
print(price2_container)


## Output - Completed output from 2017-12-20 directory
print('[')
for artist, works, currency, price in zip(artist2_container, works2_container, currency2_container, price2_container):
    out = ('  {' + '\n' 
           + '    artist: ' + "'" + artist + "'" + ', ' + '\n' 
           + '    works: ' + '[' + '\n'
           + '    { ' + "title: '" + works + "', currency: '" + currency + "', amount: '" + price + "' }," + '\n'
           +'  },' + '\n')
    print(out)
print(']')


## Task 6 - Convert the amount of all works to USD
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 
rate = 1.34 # 1 GBP = 1.34 USD

# Since only for data from 2015-03-18 has GBP currency
for i in range(len(currency_container)):
    if currency_container[i] == 'GBP':
        # convert string with commas to int for multiply
        price_container2[i] = locale.atoi(price_container2[i]) * rate
        # convert int to string with commas as thousands separators
        price_container2[i] = "{:,}".format(price_container2[i])
        currency_container[i] = 'USD'

        
# For final task, given that some of artists have multiple works;
# since artist names is unique, to return all of the work for each artist,
# consider using dictionary, where key is the artist name



## Final Task I - Preprocessing

# Before creating dictionary, I found artist name from two directories not in the same format,
# some of them along with (birth year - death year),
# clean the artist name format by removing the date for next step of pairing keys

import re
# remove everything inside brackets together with "()", and taking out the space at begining and end

for i in range(len(artist_container)):
    artist_container[i] = re.sub(r'\(.*?\)', '', artist_container[i]).strip()

for i in range(len(artist2_container)):
    artist2_container[i] = re.sub(r'\(.*?\)', '', artist2_container[i]).strip()
    
    
# To iterate through outputs from two directories, combine dataset together
Artist = artist_container + artist2_container
Works = works_container + works2_container
Currency = currency_container + currency2_container
Price = price_container2 + price2_container
