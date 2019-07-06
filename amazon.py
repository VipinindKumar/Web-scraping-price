import re

productClass = 'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'

def amazon(page_soup):
	# create a new file in write mode
	f = open('data/amazon-laptops.csv', 'w')

	# write a header, columns name
	f.write('Brand, Name, Price-was, Current-Price, Discount(₹), Discount(%), Rating, Number-of-ratings\n')

	# grabs each item-container
	conts = page_soup.findAll('div', {'class': productClass})

	for cont in conts:
		title = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div > h2 > a').get_text(strip=True)

		brand = title.split(' ')[0]
		
		try:
			rating = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(2) > div > span').get_text(strip=True)
		except:
			rating = 'NaN'
		
		try:
			num_rating = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(2) > div > a').get_text(strip=True)
		except:
			num_rating = 0
		
		price = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div').get_text(strip=True)
		
		price = re.search('₹(\d+,\d+)(?:\d+,\d+)(\d+,\d+)(?:\d+,\d+).+₹(\d+,\d+)\s\((\d+)%\)', price)
		
		pw = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > div > div > div > a > span:nth-of-type(2) > span').get_text(strip=True)[1:].replace(',', '')
		
		pc = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > div > div > div > a > span > span').get_text(strip=True)[1:].replace(',', '')
		
		disc = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > div > div > div > span:nth-of-type(2)').get_text(strip=True)
		disc = re.search('.*₹(\d+,\d+)\s\((\d+)%\)', disc)
		dc = disc.group(1).replace(',', '')
		dcp = disc.group(2)
		
		
		f.write(brand + ',' + title.replace(',', ' ') + ',' + pw + ',' + pc + ',' + dc + ',' + dcp + ',' + rating + ',' + num_rating + '\n')
	f.close()

	print('Scraped Amazon')
