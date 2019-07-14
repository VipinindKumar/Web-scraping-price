import re


def flipkart(page_soup):
	'''
	It takes the Beautiful-soup of the flipkart's page, extract the details of the products listed and write them into a csv file
	'''
	
	# create a new file to write data in csv
	f = open('data/flipkart-laptops.csv', 'w')

	# write a header, columns name
	f.write('Brand, Name, Price-was, Current-Price, Discount(₹), Discount(%), Rating(Out of 5), Number-of-ratings, RAM(GB), Storage(GB/TB)\n')

	# grabs each item-container
	conts = page_soup.findAll('div', {'class': 'bhgxx2 col-12-12'})
	conts = conts[2:-2]
	
	for cont in conts:
		# get the title of the product
		try:
			title = cont.select_one('div > div > div > a > div:nth-of-type(3) > div > div').get_text(strip=True)
		except:
			title = cont.select_one('div > div > div > a > div:nth-of-type(2) > div > div').get_text(strip=True)
		
		# retrieve the brand name of the product
		brand = title.split(' ')[0]
		
		# star rating of the product and number of reviews, if available
		try:
			rating = cont.select_one('div > div > div > a > div:nth-of-type(3) > div > div:nth-of-type(2) > span').get_text(strip=True)
						
			num_rating = cont.select_one('div > div > div > a > div:nth-of-type(3) > div > div:nth-of-type(2) > span:nth-of-type(2) > span > span').get_text(strip=True)
			num_rating = num_rating.split(' ')[0]
			
			num_review = cont.select_one('div > div > div > a > div:nth-of-type(3) > div > div:nth-of-type(2) > span:nth-of-type(2) > span > span:nth-of-type(3)').get_text(strip=True)
			num_review = num_review.split(' ')[0]
			
		except:
			rating = 'NaN'
			num_rating = '0'
			num_review = '0'
		
		# previous price of the product and discount, if available
		try:
			price = cont.select_one('div > div > div > a > div:nth-of-type(3) > div:nth-of-type(2) > div').get_text(strip=True)
			price = re.search('₹(\d+,\d+)₹(\d+,\d+)(\d\d)%', price)
			
			# previous price
			pw = price.group(2)
			# Current price of the product
			pc = price.group(1)	
								
			# discount in ruppee and percent
			dcp = price.group(3)
			
		except:
			pw = 'NaN'
			pc = 'NaN'
			dc = '0'
			dcp = '0'
		
		# ram
		try:
		 	ram = cont.select_one('div > div > div > a > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(3) > ul > li:nth-of-type(2)').get_text()
		 	ram = ram.split(' ')[0]
		 	
		except:
		 	ram = 'NaN'
		
		# Storage
		try:
		 	hdd = cont.select_one('div > div > div > a > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(3) > ul > li:nth-of-type(4)').get_text()
		 	hdd = hdd.split(' ')[0]
		 	
		except:
		 	hdd = 'NaN'

		# write the variables in csv file
		f.write(brand + ',' + title.replace(',', ' ') + ',' + pw + ',' + pc + ',' + dcp + ',' + rating + ',' + num_rating + ',' + ram + ',' + hdd + '\n')
	f.close()

	print('Scraped Flipkart')


def kartUrls(page_soup, url):
	'''
	Extract the last page number from page_soup and create urls upto that page using predefined template of the flipkart urls
	'''
	
	# get the last page number
	last = kartLast(page_soup)
	
	# Create urls to return using url template of flipkart
	


def kartLast(page_soup):
	'''
	
	'''