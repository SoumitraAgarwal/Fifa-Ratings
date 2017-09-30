# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd
import shutil
import requests.packages.urllib3
import time
requests.packages.urllib3.disable_warnings()

url = "https://b.fssta.com/uploads/application/soccer/players/"
end = ".vresize.700.850.medium.49.png"
proxies = {
  'http': 'http://.4.22.5:3128',
  'https': 'https://10.4.22.5:3128',
}

i = 345033
counts = 0
millis = int(round(time.time() * 1000))

while(True):
	if(i%100 == 0):
		rate = 0.1*counts/(int(round(time.time() * 1000)) - millis)
		print("Counts: " + str(counts) + " in " + str(int(round(time.time() * 1000)) - millis) + "ms, rate: " + str(rate) + "pictures/s")
		counts = 0

	url_temp = url+str(i)+end
	try:
		response = requests.get(url_temp, stream=True)
		if response.status_code == 200:
			counts += 1
			with open('Pictures2/'+str(i)+'.png', 'wb') as out_file:
				shutil.copyfileobj(response.raw, out_file)
			del response
	except requests.exceptions.RequestException as e:  # This is the correct syntax
		print(e)

	i += 1