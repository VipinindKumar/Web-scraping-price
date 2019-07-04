from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://www.newegg.com/global/in-en/Laptops-Notebooks/Category/ID-223?Tid=1297916'

# open connection to url, and download the page
client = urlopen(url)
page_html = client.read()
client.close()

# parse the page
page_soup = BeautifulSoup(page_html, 'html.parser')

# create a new file in write mode
f =  open('data/newegg-laptops.csv', 'w')

# write a header, columns name
f.write('Brand, Name\n')

# grabs each item-container
conts = page_soup.findAll('div', {'class': 'item-container'})

for cont in conts:
	# getting brand name from the title of img tag
	brand = cont.find('div', 'item-info').div.a.img['title']

	# getting title/name of the product
	title = cont.findAll('a', {'class': 'item-title'})[0].text

	# previous price
	pw = cont.find('div', 'item-info').find('div','item-action').ul.li.span.text

	# current price of the product
	pc = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-current').text
	pc = pc.replace(',', '')
	pc = re.search('.+\s([0-9]+).+', pc).group(1)

	# discount on the product
	dc = d = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-save').find('span','price-save-percent').text[:-1]
 
	f.write(brand + ',' + title.replace(',', ' ')
	+ pw + ',' + pc + ',' + dc + ',' + '\n')

f.close()