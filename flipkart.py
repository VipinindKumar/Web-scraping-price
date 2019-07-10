import re

def flipkart(page_soup):
	# create a new file in write mode
	f = open('data/amazon-laptops.csv', 'w')

	# write a header, columns name
	f.write('Brand, Name, Price-was, Current-Price, Discount(₹), Discount(%), Rating(Out of 5), Number-of-ratings\n')

	# grabs each item-container
	conts = page_soup.findAll('div', {'class': 'bhgxx2 col-12-12'})
	conts = conts[2:-2]
	
	for cont in conts:
		# get the title of the product
		title = cont.select_one('div > div > div > a > div:nth-of-type(3) > div > div').get_text(strip=True)
		
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
		
		# write the variables in csv file
		f.write(brand + ',' + title.replace(',', ' ') + ',' + pw + ',' + pc + ',' + dc + ',' + dcp + ',' + rating + ',' + num_rating + '\n')
	f.close()

	print('Scraped Amazon')