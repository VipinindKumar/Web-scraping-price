from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://www.amazon.in/s?bbn=1375424031&rh=n%3A976392031%2Cn%3A976393031%2Cn%3A1375424031%2Cp_36%3A7252028031&dc&fst=as%3Aoff&rnid=7252027031'
client = urlopen(url)
page_html = client.read()
client.close()
page_soup = BeautifulSoup(page_html, 'html.parser')
conts = page_soup.findAll('div', {'class': 'bhgxx2 col-12-12'})
cont = conts[0]
