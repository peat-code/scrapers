from bs4 import BeautifulSoup
import requests
import pandas
data = []


rec = requests.get("https://redditlist.com/all1")

soup = BeautifulSoup(rec.text,'html.parser')

sub_table = soup.find('div',attrs={'id':'listing-parent'}).select("div:nth-of-type(2)")

for table in sub_table:

    items = table.find_all('div',attrs={'class':'listing-item'})

    for item in items:
        name = item.attrs["data-target-subreddit"]
        filternsfw = item.attrs["data-target-filter"]
        link = item.find('a')['href']
        rank = item.find('span',attrs={'class':'rank-value'}).text
        data.append((name,filternsfw,link,rank))




    table = pandas.DataFrame(data,columns=['Name','Filter','Link','Rank'])
    table.to_csv('subs.csv',index=False,encoding='utf-8')
