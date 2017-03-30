# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests

url = "https://www.fifaindex.com/"
proxies = {
  'http': 'http://10.4.22.5:3128',
  'https': 'https://10.4.22.5:3128',
}

page = requests.get(url,proxies=proxies)

html = page.content
soup = BeautifulSoup(html,'lxml')
right_table=soup.find('table', class_='table table-striped players')

A=[]
B=[]
C=[]

for row in right_table.findAll("tr"):
    cells = row.find("td")
    if(cells!=None):
    	a = cells.find("a")
    	if(a!=None):
	    	A.append(a["title"])
	        B.append(a["href"])
print(A)
# print(B)
# print(C)

