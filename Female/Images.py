# -*- coding: utf-8 -*-
import os
import cv2
import pandas as pd
import requests
from bs4 import BeautifulSoup
import shutil

base = 'Pictures/'
a = os.listdir(base)
incorrect = [];


df = pd.read_csv("Names.csv")

print("Read complete")


url = "https://www.fifaindex.com"
proxies = {
  'http': 'http://a.soumitra:boo<3cha@202.141.80.22:3128',
  'https': 'https://a.soumitra:boo<3cha@202.141.80.22:3128',
}
for i in range(len(a)):
    im = cv2.imread(base+a[i])
    if(im is None):
    	incorrect.append(a[i])

row = [];
for element in incorrect:
	row.append(df[df['Name']==element]['url'])
	print(element)
	os.remove(base+element)

# print(len(incorrect))
# for i in range(len(row)):
# 	for parts in row[i]:
# 		url_temp = url+parts
# 		while(True):
# 			print("Getting page "+url_temp)
# 			try:
# 				page = requests.get(url_temp,proxies=proxies)
# 			except requests.exceptions.RequestException as e:  # This is the correct syntax
# 				print(e)
# 				continue
# 			break

# 		html = page.content
# 		soup = BeautifulSoup(html,'lxml')
		
# 		Nat = soup.find('img')
# 		while(True):
# 			try:
# 				response = requests.get(url+Nat['src'], stream=True,proxies=proxies)
# 			except requests.exceptions.RequestException as e:  # This is the correct syntax
# 				print(e)
# 				continue
# 			break
# 		with open('Pictures/'+incorrect[i]+'.png', 'wb') as out_file:
# 			shutil.copyfileobj(response.raw, out_file)
# 		del response