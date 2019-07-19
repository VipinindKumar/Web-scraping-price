from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://www.newegg.com/global/in-en/Laptops-Notebooks/SubCategory/ID-32?Tid=1297918'
client = urlopen(url)
page_html = client.read()
client.close()
page_soup = BeautifulSoup(page_html, 'html.parser')
conts = page_soup.findAll('div', {'class': 'item-container'})
cont = conts[0]
