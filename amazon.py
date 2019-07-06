import re

productClass = 'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'

def amazon(page_soup):
	# create a new file in write mode
	f = open('data/amazon-laptops.csv', 'w')

	# write a header, columns name
	f.write('Brand, Name, Price-was, Current-Price, Discount(%)\n')

	# grabs each item-container
	conts = page_soup.findAll('div', {'class': productClass})

	for cont in conts:
		name = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div > h2 > a').get_text(strip=True)

		brand = name.split(' ')[0]
		
		rating = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(2) > div > span').get_text(strip=True)
		
		num_rating = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(2) > div > a').get_text(strip=True)
		
		price = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div').get_text(strip=True)
		
		price = re.search('₹(\d+,\d+)(?:\d+,\d+)(\d+,\d+)(?:\d+,\d+).+₹(\d+,\d+)\s\((\d+)%\)', price)
		
		pw = price.group(2).replace(',', '')
		pc = price.group(1).replace(',', '')
		dc = price.group(3).replace(',', '')
		dcp = price.group(4)
		
		
		f.write('')
	f.close()

	print('Scraped Amazon')
