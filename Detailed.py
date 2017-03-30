# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd

df = pd.read_csv("PlayerNames.csv")

print("Read complete")


url = "https://www.fifaindex.com"
proxies = {
  'http': 'http://10.4.22.5:3128',
  'https': 'https://10.4.22.5:3128',
}



Name = [];
Height = [];
Weight = [];
Preffered_foot = [];
Birth_date = [];
Age = [];
Preffered_position = [];
Work_rate = [];
Weak_foot = [];
Skill_moves = [];






for i in range(len(df['Name'])):
	Name.append(df['Name'][i])
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
	right_table=soup.find('div', class_='panel-body')
	

	Para = right_table.findAll('p')
	
	Attributes = Para[0].findAll('span')
	Height.append(str(Attributes[0].find(text=True)))
	
	Attributes = Para[1].findAll('span')
	Weight.append(str(Attributes[0].find(text=True)))
	
	Attributes = Para[2].findAll('span')
	temp = ''
	for i in range(len(Attributes)-1):
		temp = temp + str(Attributes[i].find(text=True)) + '/'
	temp = temp + str(Attributes[len(Attributes)-1].find(text=True))
	Preffered_foot.append(str(temp))
	
	Attributes = Para[3].findAll('span')
	Birth_date.append(str(Attributes[0].find(text=True)))
	

	Attributes = Para[4].findAll('span')
	Age.append(str(Attributes[0].find(text=True)))
	
	Attributes = Para[5].findAll('span')
	temp = ''
	for i in range(1,len(Attributes)-1,2):
		temp = temp + str(Attributes[i].find(text=True)) + '/'
	temp = temp + str(Attributes[len(Attributes)-1].find(text=True))
	Preffered_position.append(temp)
	
	Attributes = Para[6].findAll('span')
	temp = ''
	for i in range(len(Attributes)-1):
		temp = temp + str(Attributes[i].find(text=True)) + '/'
	temp = temp + str(Attributes[len(Attributes)-1].find(text=True))
	Work_rate.append(temp)

	Attributes = Para[7].findAll('span', class_="star")
	stars = Attributes[0].findAll('i', class_="fa fa-star fa-lg")
	Weak_foot.append(len(stars))

	Attributes = Para[8].findAll('span', class_="star")
	stars = Attributes[0].findAll('i', class_="fa fa-star fa-lg")
	Skill_moves.append(len(stars))

	
	break
df1 = pd.DataFrame({'Name' : Name, 'Height' : Height, 'Weight' : Weight, 'Preffered_Foot': Preffered_foot,
	'Birth_Date': Birth_date, 'Age': Age, 'Preffered_Position' : Preffered_position, 'Work_Rate': Work_rate,
	'Weak_foot' : Weak_foot, 'Skill_Moves' : Skill_moves})
print(df1)
# df.to_csv('Names.csv', index = False, encoding = 'utf-8')

