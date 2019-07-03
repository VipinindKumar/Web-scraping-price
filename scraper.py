from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.newegg.com/global/in-en/Laptops-Notebooks/Category/ID-223?Tid=1297916'

# open connection to url, and download the page
client = urlopen(url)
page_html = client.read()
client.close()

# parse the page
page_soup = BeautifulSoup(page_html, 'html.parser')

# create a new file in write mode
f =  open('laptops.csv', 'w')

# write a header, columns name
f.write('Brand, Name\n')

# grabs each item-container
conts = page_soup.findAll('div', {'class': 'item-container'})

for cont in conts:
	brand = cont.find('div', 'item-info').div.a.img['title']

	name = cont.findAll('a', {'class': 'item-title'})[0].text

	f.write(brand + ',' + name.replace(',', ' ') + '\n')

f.close()