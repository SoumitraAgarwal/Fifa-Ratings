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
Nationality = [];
Rating = [];
Height = [];
Weight = [];
Preffered_foot = [];
Birth_date = [];
Age = [];
Preffered_position = [];
Work_rate = [];
Weak_foot = [];
Skill_moves = [];
Teams = [];
National_position = [];
National_kit = [];
Position = [];
Kit = [];
Joining = [];
Contract = [];
Ball_Control = [];
Dribbling = [];
Marking = [];
Sliding = [];
Standing = [];
Aggression = [];
Reaction = [];
Attack = [];
Interceptions = [];
Vision = [];
Composure = [];
Crossing = [];
Short_pass = [];
Long_pass = [];
Acceleration = [];
Stamina = [];
Strength = [];
Balance = [];
Sprint = [];
Agility = [];
Jumping = [];
Heading = [];
Shot_power = [];
Finishing = [];
Long_shots = [];
Curve = [];
Freekick = [];
Penalties = [];
Volleys = [];
GK_Posi = [];
GK_Diving = [];
GK_Kick = [];
GK_Handling = [];
GK_Reflexes = [];



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
	
	Nat = soup.find('h2', class_="subtitle")
	Pos = Nat.find('a')
	Nationality.append(Pos.find(text=True))

	Team = soup.findAll('div', class_="panel-heading")
	Club = Team[2].findAll('a')
	Teams.append(Club[1].find(text=True))

	Panels = soup.find('h3', class_="panel-title")
	Rate = Panels.findAll('span')
	Rating.append(Rate[1].find(text=True))


	right_table=soup.findAll('div', class_='panel-body')
	Para = right_table[0].findAll('p')
	
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

	Both = soup.findAll('div',class_="col-lg-4 col-md-5 col-sm-6 col-ms-6 col-xs-12 team")
	done = 1
	if(len(Both)==2):
		Para = right_table[1].findAll('p')
		Attributes = Para[0].findAll('span')
		National_position.append(str(Attributes[1].find(text=True)))

		Attributes = Para[1].findAll('span')
		National_kit.append(str(Attributes[0].find(text=True)))
	

		Para = right_table[2].findAll('p')
		Attributes = Para[0].findAll('span')
		Position.append(str(Attributes[1].find(text=True)))

		Attributes = Para[1].findAll('span')
		Kit.append(str(Attributes[0].find(text=True)))

		Attributes = Para[2].findAll('span')
		Joining.append(str(Attributes[0].find(text=True)))
	
		Attributes = Para[3].findAll('span')
		Contract.append(str(Attributes[0].find(text=True)))
		done = done + 1
	
	else:
		Para = right_table[1].findAll('p')
		Attributes = Para[0].findAll('span')
		Position.append(str(Attributes[1].find(text=True)))

		Attributes = Para[1].findAll('span')
		Kit.append(str(Attributes[0].find(text=True)))

		Attributes = Para[2].findAll('span')
		Joining.append(str(Attributes[0].find(text=True)))
	
		Attributes = Para[3].findAll('span')
		Contract.append(str(Attributes[0].find(text=True)))
	

	done = done + 1;
	
	
	Para = right_table[done].findAll('p')
	Attributes = Para[0].findAll('span')
	Ball_Control.append(str(Attributes[1].find(text=True)))

	Attributes = Para[1].findAll('span')
	Dribbling.append(str(Attributes[1].find(text=True)))


	done = done + 1;
	
	Para = right_table[done].findAll('p')
	Attributes = Para[0].findAll('span')
	Marking.append(str(Attributes[1].find(text=True)))

	Attributes = Para[1].findAll('span')
	Sliding.append(str(Attributes[1].find(text=True)))


	Attributes = Para[2].findAll('span')
	Standing.append(str(Attributes[1].find(text=True)))


	done = done + 1;
	
	Para = right_table[done].findAll('p')
	Attributes = Para[0].findAll('span')
	Aggression.append(str(Attributes[1].find(text=True)))

	Attributes = Para[1].findAll('span')
	Reaction.append(str(Attributes[1].find(text=True)))


	Attributes = Para[2].findAll('span')
	Standing.append(str(Attributes[1].find(text=True)))

	Attributes = Para[3].findAll('span')
	Attack.append(str(Attributes[1].find(text=True)))

	Attributes = Para[4].findAll('span')
	Interceptions.append(str(Attributes[1].find(text=True)))

	Attributes = Para[5].findAll('span')
	Vision.append(str(Attributes[1].find(text=True)))


	done = done + 1;
	
	Para = right_table[done].findAll('p')
	Attributes = Para[0].findAll('span')
	Crossing.append(str(Attributes[1].find(text=True)))

	Attributes = Para[1].findAll('span')
	Short_pass.append(str(Attributes[1].find(text=True)))


	Attributes = Para[2].findAll('span')
	Long_pass.append(str(Attributes[1].find(text=True)))



	done = done + 1;
	
	Para = right_table[done].findAll('p')
	Attributes = Para[0].findAll('span')
	Acceleration.append(str(Attributes[1].find(text=True)))

	Attributes = Para[1].findAll('span')
	Stamina.append(str(Attributes[1].find(text=True)))


	Attributes = Para[2].findAll('span')
	Strength.append(str(Attributes[1].find(text=True)))

	Attributes = Para[3].findAll('span')
	Balance.append(str(Attributes[1].find(text=True)))

	Attributes = Para[4].findAll('span')
	Sprint.append(str(Attributes[1].find(text=True)))

	Attributes = Para[5].findAll('span')
	Agility.append(str(Attributes[1].find(text=True)))

	Attributes = Para[6].findAll('span')
	Jumping.append(str(Attributes[1].find(text=True)))



	done = done + 1;
	
	Para = right_table[done].findAll('p')
	Attributes = Para[0].findAll('span')
	Heading.append(str(Attributes[1].find(text=True)))

	Attributes = Para[1].findAll('span')
	Shot_power.append(str(Attributes[1].find(text=True)))

	Attributes = Para[2].findAll('span')
	Finishing.append(str(Attributes[1].find(text=True)))

	Attributes = Para[3].findAll('span')
	Long_shots.append(str(Attributes[1].find(text=True)))

	Attributes = Para[4].findAll('span')
	Curve.append(str(Attributes[1].find(text=True)))

	Attributes = Para[5].findAll('span')
	Freekick.append(str(Attributes[1].find(text=True)))

	Attributes = Para[6].findAll('span')
	Penalties.append(str(Attributes[1].find(text=True)))

	Attributes = Para[7].findAll('span')
	Volleys.append(str(Attributes[1].find(text=True)))



	done = done + 1;
	
	Para = right_table[done].findAll('p')
	Attributes = Para[0].findAll('span')
	GK_Posi.append(str(Attributes[1].find(text=True)))

	Attributes = Para[1].findAll('span')
	GK_Diving.append(str(Attributes[1].find(text=True)))

	Attributes = Para[2].findAll('span')
	GK_Handling.append(str(Attributes[1].find(text=True)))

	Attributes = Para[3].findAll('span')
	GK_Kick.append(str(Attributes[1].find(text=True)))

	Attributes = Para[4].findAll('span')
	GK_Reflexes.append(str(Attributes[1].find(text=True)))


df1 = pd.DataFrame({'Name' : Name, 'Nationality': Nationality, 'National_Position' : National_position, 
	'National_Kit' : National_kit,'Club' : Teams,'Club_Position' : Position, 'Club_Kit' : Kit,
	'Club_Joining' : Joining, 'Contract_Expiry' : Contract, 'Rating' : Rating, 'Height' : Height,
	'Weight' : Weight, 'Preffered_Foot': Preffered_foot,'Birth_Date': Birth_date, 'Age': Age, 
	'Preffered_Position' : Preffered_position, 'Work_Rate': Work_rate,'Weak_foot' : Weak_foot,
	'Skill_Moves' : Skill_moves, 'Ball_Control': Ball_Control, 'Dribbling': Dribbling})


cols = ['Name', 'Nationality', 'National_Position', 'National_Kit', 'Club', 'Club_Position', 'Club_Kit',
		'Club_Joining', 'Contract_Expiry', 'Rating', 'Height', 'Weight', 'Preffered_Foot', 'Birth_Date',
		'Age', 'Preffered_Position', 'Work_Rate', 'Weak_foot', 'Skill_Moves', 'Ball_Control', 'Dribbling']

df1 = df1[cols]
print(df1)
# df.to_csv('Names.csv', index = False, encoding = 'utf-8')

