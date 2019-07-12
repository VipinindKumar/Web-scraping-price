import re

def newegg(page_soup):
	# create a new file in write mode
	f =  open('data/newegg-laptops.csv', 'w')

	# write a header, columns name
	f.write('Brand, Name, Price-was, Current-Price, Discount(%), RAM(GB), Storage(GB/TB)\n')

	# grabs each item-container
	conts = page_soup.findAll('div', {'class': 'item-container'})

	for i,cont in enumerate(conts):
		print(i)
		# getting brand name from the title of img tag
		# to filter products pop up shown in recently viewed items at the end of the page
		try:
			brand = cont.find('div', 'item-info').div.a.img['title']
		except:
			continue

		# getting title/name of the product
		title = cont.findAll('a', {'class': 'item-title'})[0].text
		
		# process title to extract ram, storage
		features = title.replace(' ', '')
		features = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', features)
		
		ram = features.group(1)
		hdd = features.group(2)
		
		try:
			# previous price, if available
			pw = cont.find('div', 'item-info').find('div','item-action').ul.li.span.text
			
			# discount on the product, if available
			dc = d = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-save').find('span','price-save-percent').text[:-1]
		except:
			pw = 'NaN'
			dc = '0'
		
		# current price of the product
		pc = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-current').text
		pc = pc.replace(',', '')
		pc = re.search('.+\s([0-9]+).+', pc).group(1)
		
		
		# write the row into csv file
		f.write(brand + ',' + title.replace(',', ' ')
		+ ',' + pw + ',' + pc + ',' + dc + ',' + ram + ',' + hdd + '\n')

	f.close()

	print('Scraped Newegg')