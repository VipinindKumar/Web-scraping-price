import re

def newegg(page_soup):
	# create a new file in write mode
	f =  open('data/newegg-laptops.csv', 'w')

	# write a header, columns name
	f.write('Brand, Name, Price-was, Current-Price, Discount(%), RAM(GB), Storage(GB/TB), Refurbished(0/1)\n')

	# grabs each item-container
	conts = page_soup.findAll('div', {'class': 'item-container'})

	for cont in conts:
		# getting brand name from the title of img tag
		try:
			brand = cont.find('div', 'item-info').div.a.img['title']
		except:
			brand = 'NaN'
		
		# to filter products pop up shown in recently viewed items at the end of the page
		# print(brand)
		# if not brand:
		# 	continue

		# getting title/name of the product
		title = cont.findAll('a', {'class': 'item-title'})[0].text
		
		# if product is refurbished/renewed
		if ('refurbished' in title.lower()) or ('renewed' in title.lower()):
			refurb = 1
		else:
			refurb = 0
		
		# process title to extract ram, storage
		features = title.replace(' ', '')
		features = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', features)
		
		# some products doesn't contain this inforamtion
		try:
			ram = features.group(1)
			hdd = features.group(2)
		except:
			ram = 'NaN'
			hdd = 'NaN'
		
		# PRICE
		try:
			# previous price, if available
			pw = cont.find('div', 'item-info').find('div','item-action').ul.li.span.text
			
			# discount on the product, if available
			dc = d = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-save').find('span','price-save-percent').text[:-1]
		except:
			pw = 'NaN'
			dc = '0'
		
		# current price of the product
		try:
			pc = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-current').text
			pc = pc.replace(',', '')
			pc = re.search('.+\s([0-9]+).+', pc).group(1)
		except:
			pc = 'NaN'
		
		
		# write the row into csv file
		f.write(brand + ',' + title.replace(',', ' ')
		+ ',' + pw + ',' + pc + ',' + dc + ',' + ram + ',' + hdd + ',' + refurb + '\n')

	f.close()

	print('Scraped Newegg\'s page')



def eggUrls(page_soup, url):
	'''
	Extract the last page number from page_soup and create urls upto that page using predefined template of the newegg urls
	'''
	
	# get the last page number
	last = eggLast(page_soup)
	
	urls = list()
	# Create urls to return using url template of flipkart
	for i in range(2, last+1):
		url = 'https://www.newegg.com/global/in-en/Laptops-Notebooks/SubCategory/ID-32/Page-' + str(i) + '?Tid=1297918'
		
		urls.append(url)
	
	return urls		


def eggLast(page_soup):
	'''
	Return the last page number from the page
	'''
	
	last = page_soup.findAll('div', {'class': 'page_NavigationBar'})[1]
	last = last.select_one('div:nth-of-type(10)').text.strip()
	
	return int(last)