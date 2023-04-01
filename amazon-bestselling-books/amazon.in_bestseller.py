import requests
from bs4 import BeautifulSoup
import pandas
data=[]
for i in range(1,2):
	rec=requests.get("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_"+str(i)+"?ie=UTF8&pg="+str(i))
	soup=BeautifulSoup(rec.text,'html.parser')
	records=soup.find_all('div', attrs={'class':'_cDEzb_grid-column_2hIsc'})
	for record in records:
		try:
			name=record.find('div',attrs={'class':'_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'}).text
		except:
			name="Not Available"
		try:
			url="https://www.amazon.in" + record.find('a',attrs={'class':'a-link-normal'})['href']
		except:
			url="Not Available"
		try:
			author=record.find('div',attrs={'class':'a-row a-size-small'}).text
		except:
			author="Not Available"
		try:
			price=record.find('span',attrs={'class':'p13n-sc-price'}).text
		except:
			price="Not Available"
		
		try:
			rating=record.find('span',attrs={'class':'a-icon-alt'}).text[0:3]
		except:
			rating="Not Available"
			stars="Not Available"
		try:
			stars = record.find('div',attrs={'class':'a-icon-row'})
			stars = stars.find('span',attrs={'class':'a-size-small'}).text
			#stars=record.find('span',attrs={'class':'a-size-small'}).text
			print(stars)
		except:
			stars="Not Available"
		# print(rating,stars)
		data.append((name,url,author,price,rating,stars))
table = pandas.DataFrame(data,columns=['Name','URL','Author','Price','Average Rating','Number of Ratings'])
table.to_csv('in_book.csv',index=False,encoding='utf-8') 
