def flipkart(page_soup):
	# create a new file in write mode
	f = open('data/amazon-laptops.csv', 'w')

	# write a header, columns name
	f.write('Brand, Name, Price-was, Current-Price, Discount(₹), Discount(%), Rating(Out of 5), Number-of-ratings\n')

	# grabs each item-container
	conts = page_soup.findAll('div', {'class': productClass})

	for cont in conts:
		# get the title of the product
		title = 
		
		# retrieve the brand name of the product
		brand = title.split(' ')[0]
		
		# star rating of the product and number of reviews, if available
		try:
			rating = 
			
			num_rating = 
			except:
			rating = 'NaN'
			num_rating = '0'
		
		# previous price of the product and discount, if available
		try:
			# previous price
			pw = 
						
			# discount in ruppee and percent
			
		except:
			pw = 'NaN'
			dc = '0'
			dcp = '0'
		
		try:
			# Current price of the product
			pc = 
		except:
			pc = 'NaN'
		
		
		# write the variables in csv file
		f.write(brand + ',' + title.replace(',', ' ') + ',' + pw + ',' + pc + ',' + dc + ',' + dcp + ',' + rating + ',' + num_rating + '\n')
	f.close()

	print('Scraped Amazon')