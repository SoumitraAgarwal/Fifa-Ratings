# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd

url1 = "https://www.fifaindex.com/"
url = "https://www.fifaindex.com/players/?gender=1"
proxies = {
  'http': 'http://a.soumitra:boo<3cha@202.141.80.22:3128',
  'https': 'https://a.soumitra:boo<3cha@202.141.80.22:3128',
}

page = requests.get(url,proxies=proxies)

html = page.content
soup = BeautifulSoup(html,'lxml')
right_table=soup.find('table', class_='table table-striped players')

A=[]
B=[]

for row in right_table.findAll("tr"):
    cells = row.find("td")
    if(cells!=None):
    	a = cells.find("a")
    	if(a!=None):
	    	A.append(a["title"])
	        B.append(a["href"])

temp_df=pd.DataFrame({'Name':A, 'url' : B})
print(temp_df)

for i in range(2,12):
	print(i)
	url_temp = url1+'/players/'+str(i)+'/?gender=1'
	
	while(True):
		print("Getting page "+str(i))
		try:
			page = requests.get(url_temp,proxies=proxies)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break

	html = page.content
	soup = BeautifulSoup(html,'lxml')
	right_table=soup.find('table', class_='table table-striped players')

	for row in right_table.findAll("tr"):
	    cells = row.find("td")
	    if(cells!=None):
	    	a = cells.find("a")
	    	if(a!=None):
		    	A.append(a["title"])
		        B.append(a["href"])
	df=pd.DataFrame({'Name':A, 'url' : B})
	print(df)
df.to_csv('Names.csv', index = False, encoding = 'utf-8')

