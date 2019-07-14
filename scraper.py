from urllib.request import urlopen
from bs4 import BeautifulSoup

from newegg import newegg
from amazon import amazon
from flipkart import flipkart

urls = ['https://www.newegg.com/global/in-en/Laptops-Notebooks/SubCategory/ID-32?Tid=1297918', 
'https://www.amazon.in/s?bbn=1375424031&rh=n%3A976392031%2Cn%3A976393031%2Cn%3A1375424031%2Cp_36%3A7252028031&dc&fst=as%3Aoff&rnid=7252027031', 
'https://www.flipkart.com/laptops/pr?sid=6bo%2Fb5g&p%5B%5D=sort%3Dpopularity&p%5B%5D=facets.price_range.to%3D25000&p%5B%5D=facets.price_range.from%3D15000&fm=neo%2Fmerchandising&iid=M_3580c4f9-a714-45e8-a54c-64fa60d4b35d_10.f37da198-ab3e-48f0-bc9a-12dfbbbc32c9_DesktopSite&ppt=clp&ppn=laptops-store']

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
		# add function call that will create urls to be appended to the list urls, function will get the last page number and create urls upto that page using predefined template for next pages
		
		amazon(page_soup)
	
	if 'flipkart' in url:
		flipkart(page_soup)