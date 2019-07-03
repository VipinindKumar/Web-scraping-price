from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.newegg.com/global/in-en/Laptops-Notebooks/Category/ID-223?Tid=1297916'

# open connection to url, and download the page
client = urlopen(url)
page_html = client.read()
client.close()

# parse the page
page_soup = BeautifulSoup(page_html, 'html.parser')
