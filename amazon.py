import re

productClass = 'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'

def amazon(page_soup):
	'''
	It takes the Beautiful-soup of the amazon's page, extract the details of the products listed and write them into a csv file	
	'''
	
	# create a new file in write mode
	f = open('data/amazon-laptops.csv', 'w')

	# write a header, columns name
	f.write('Brand, Name, Price-was, Current-Price, Discount(₹), Discount(%), Rating(Out of 5), Number-of-ratings, RAM(GB), Storage(GB/TB)\n')

	# grabs each item-container
	conts = page_soup.findAll('div', {'class': productClass})

	for cont in conts:
		# get the title of the product
		title = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div > h2 > a').get_text(strip=True)
		
		# process title to extract ram, storage
		features = title.replace(' ', '').replace('-', '/')
		
		features = re.search('.+(\d+)GB.*/(\d+)(?:G|T).*', features)
		
		ram = features.group(1)
		hdd = features.group(2)
		
		
		# retrieve the brand name of the product
		brand = title.split(' ')[0]
		
		# star rating of the product and number of reviews, if available
		try:
			rating = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(2) > div > span').get_text(strip=True)
			rating = rating.split(' ')[0]
			
			num_rating = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(2) > div > a').get_text(strip=True)
		except:
			rating = 'NaN'
			num_rating = '0'
		
		# previous price of the product and discount, if available
		try:
			# previous price
			pw = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > div > div > div > a > span:nth-of-type(2) > span').get_text(strip=True)[1:].replace(',', '')
			
			# discount in ruppee and percent
			disc = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > div > div > div > span:nth-of-type(2)').get_text(strip=True)
			disc = re.search('.*₹(\d+,\d+)\s\((\d+)%\)', disc)
			dc = disc.group(1).replace(',', '')
			dcp = disc.group(2)
		except:
			pw = 'NaN'
			dc = '0'
			dcp = '0'
		
		try:
			# Current price of the product
			pc = cont.select_one('div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > div > div > div > a > span > span').get_text(strip=True)[1:].replace(',', '')
		except:
			pc = 'NaN'
		
		
		# write the variables in csv file
		f.write(brand + ',' + title.replace(',', ' ') + ',' + pw + ',' + pc + ',' + dc + ',' + dcp + ',' + rating + ',' + num_rating + ',' + ram + ',' + hdd + '\n')
	f.close()

	print('Scraped Amazon')



def zonUrls(page_soup, url):
	'''
	Extract the last page number from page_soup and create urls upto that page using predefined template of the amazon urls
	'''
	
	# get the last page number
	last = zonLast(page_soup)
	
	urls = list()
	# Create urls to return using url template of flipkart
	for i in range(2, last+1):
		url = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Fb5g&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&fm=neo%2Fmerchandising&iid=M_3580c4f9-a714-45e8-a54c-64fa60d4b35d_10.f37da198-ab3e-48f0-bc9a-12dfbbbc32c9_DesktopSite&ppt=clp&ppn=laptops-store&page=' + str(i)
		
		urls.append(url)
	
	return urls		


def zonLast(page_soup):
	'''
	Return the last page number from the page
	'''
	
	last = page_soup.find('div', {'class': '_2zg3yZ'})
	last = last.span.text.split(' ')[-1]
	
	return int(last)