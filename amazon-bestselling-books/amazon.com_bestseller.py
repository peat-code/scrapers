import requests
from bs4 import BeautifulSoup
import pandas
data=[]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

for i in range(1,2):
	rec=requests.get("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg="+str(i),headers=headers) #+str(i)+"?_encoding=UTF8&pg="+str(i))
	soup=BeautifulSoup(rec.text,'html.parser')
	
	records=soup.find_all('div', attrs={'id':'gridItemRoot'})
	for record in records:
		try:
			name=record.find('div',attrs={'class':'_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'}).text
		except:
			name="Not Available"
		try:
			url="https://www.amazon.com" + record.find('a',attrs={'class':'a-link-normal'})['href']
		except:
			url="Not Available"
		try:
			author=record.find('div',attrs={'class':'a-row a-size-small'}).text
		except:
			author="Not Available"
		try:
			price=record.find('span',attrs={'class':'a-color-price'}).text
		except:
			price="Not Available"
		try:
			stars = record.find('div',attrs={'class':'a-icon-row'})
			stars = stars.find('span',attrs={'class':'a-size-small'}).text
			
			
		except:
			stars="Not Available"
		try:
			rating=record.find('span',attrs={'class':'a-icon-alt'}).text[0:3]
			
		except:
			rating="Not Available"
			stars="Not Available"
		data.append((name,url,author,price,rating,stars))
table = pandas.DataFrame(data,columns=['Name','URL','Author','Price','Average Rating','Number of Ratings'])
table.to_csv('com_book.csv',index=False,encoding='utf-8')