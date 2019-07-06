productClass = 'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'

def amazon(page_soup):
	# create a new file in write mode
	f =  open('data/amazon-laptops.csv', 'w')

	# write a header, columns name
	f.write('Brand, Name, Price-was, Current-Price, Discount(%)\n')

	# grabs each item-container
	conts = page_soup.findAll('div', {'class': productClass})

	for cont in conts:





		f.write('')
	f.close()

	print('Scraped Amazon')
