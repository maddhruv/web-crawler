import requests
from bs4 import BeautifulSoup


def single_item(item_link):
	#for price
	source_code=requests.get(item_link)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	#price=[]
	for amzn_item_price in soup.findAll('div', {'id':'averageCustomerReviewRating'}):			
		p = amzn_item_price.string
		#price.append(p)
		print (p)

def spider():
	url="http://www.amazon.in/b?ie=UTF8&node=1388921031"
	source_code= requests.get(url)		
	plain_text= source_code.text
	soup = BeautifulSoup(plain_text, "lxml")
	#title=[]
	for amzn_item_title in soup.findAll('a', {'class':'acs_product-title'}):
		t = amzn_item_title.string
		href= "https://amazon.in/" + amzn_item_title.get('href')
		print(href)
		#title.append(t)
		print(t)
		single_item(href)

	#for n in range(0,len(title)):
		#print(str(title[n])+" with price: ")

	
spider()
