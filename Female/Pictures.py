# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd
import shutil

df = pd.read_csv("Names.csv")

print("Read complete")


url = "https://www.fifaindex.com"
proxies = {
  'http': 'http://a.soumitra:boo<3cha@202.141.80.22:3128',
  'https': 'https://a.soumitra:boo<3cha@202.141.80.22:3128',
}

for i in range(1100):
	print(i)
	url_temp = url+df['url'][i]
	while(True):
		print("Getting page for "+df['Name'][i])
		try:
			page = requests.get(url_temp,proxies=proxies)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break

	html = page.content
	soup = BeautifulSoup(html,'lxml')
	
	Nat = soup.find('img')
	print(Nat['src'])
	while(True):
		try:
			response = requests.get(url+Nat['src'], stream=True,proxies=proxies)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break
	with open('Pictures/'+df['Name'][i]+'.png', 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response