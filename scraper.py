from urllib.request import urlopen
from bs4 import BeautifulSoup

from newegg import newegg

urls = ['https://www.newegg.com/global/in-en/Laptops-Notebooks/Category/ID-223?Tid=1297916'
		]
for url in urls:
	# open connection to url, and download the page
	client = urlopen(url)
	page_html = client.read()
	client.close()

	# parse the page
	page_soup = BeautifulSoup(page_html, 'html.parser')

	# extract information and write in csv 
	if 'newegg' in url:
		#from newegg
		newegg(page_soup)

