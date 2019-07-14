from urllib.request import urlopen
from bs4 import BeautifulSoup

from newegg import newegg
from amazon import amazon, zonUrls
from flipkart import flipkart, kartUrls


def parse(url):
	'''
	Parses the url page and return a BeautifulSoup object
	'''
	
	# open connection to url, and download the page
	client = urlopen(url)
	page_html = client.read()
	client.close()

	# parse the page
	page_soup = BeautifulSoup(page_html, 'html.parser')
	
	return page_soup


urls = ['https://www.newegg.com/global/in-en/Laptops-Notebooks/SubCategory/ID-32?Tid=1297918', 
'https://www.amazon.in/s?bbn=1375424031&rh=n%3A976392031%2Cn%3A976393031%2Cn%3A1375424031%2Cp_36%3A7252028031&dc&fst=as%3Aoff&rnid=7252027031', 
'https://www.flipkart.com/laptops/pr?sid=6bo%2Fb5g&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&fm=neo%2Fmerchandising&iid=M_3580c4f9-a714-45e8-a54c-64fa60d4b35d_10.f37da198-ab3e-48f0-bc9a-12dfbbbc32c9_DesktopSite&ppt=clp&ppn=laptops-store']

# craete urls for other pages and them to the list of pages to be parsed
for url in urls:
	page_soup = parse(url)
	
	# if 'newegg' in url:
	# 	urls = urls + eggUrls(page_soup, url)
	
	if 'amazon' in url:
		urls = urls + zonUrls(page_soup, url)

	# if 'flipkart' in url:
	# 	urls = urls + kartUrls(page_soup, url)


# extract product's information and write them in csv files
for i,url in enumerate(urls):
	page_soup = parse(url)
	
	print(str(i+1) + ' Page')
	
	if 'newegg' in url:
		newegg(page_soup)

	if 'amazon' in url:		
		amazon(page_soup)
	
	if 'flipkart' in url:
		flipkart(page_soup)

