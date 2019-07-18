from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Fb5g&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&fm=neo%2Fmerchandising&iid=M_3580c4f9-a714-45e8-a54c-64fa60d4b35d_10.f37da198-ab3e-48f0-bc9a-12dfbbbc32c9_DesktopSite&ppt=clp&ppn=laptops-store'
client = urlopen(url)
page_html = client.read()
client.close()
page_soup = BeautifulSoup(page_html, 'html.parser')
conts = page_soup.findAll('div', {'class': 'bhgxx2 col-12-12'})
cont = conts[0]
