from urllib.request import urlopen
from bs4 import BeautifulSoup

from newegg import newegg

#urls = ['https://www.newegg.com/global/in-en/Laptops-Notebooks/Category/ID-223?Tid=1297916',
urls = ['https://www.amazon.in/s?bbn=1375424031&rh=n%3A976392031%2Cn%3A%21976393031%2Cn%3A1375424031%2Cp_36%3A7252028031&dc&fst=as%3Aoff&qid=1562389178&rnid=7252027031']
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

	if 'amazon' in url:
		amazon(page_soup)