import sys
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import xml

option = sys.argv[1]
 
# python3 ./p5.py -x city1,state1 city2,state2
# 58.4 km  between  murfreesboro,tn and nashville,tn
if option == "-x":
	cs1 = sys.argv[2]
	cs2 = sys.argv[3]
	
	url = 'https://maps.googleapis.com/maps/api/distancematrix/xml?origins=%s&destinations=%s' % (cs1, cs2)
	req = requests.get(url)
	soup = bs(req.content, 'html.parser')
	dist = soup.find_all('distance')
	dist = dist[0].text.split()
	dist = dist[1] +' ' + dist[2]
	print(dist,"between", cs1, "and", cs2)

# -j done
if option == "-j":
	cs1 = sys.argv[2]
	cs2 = sys.argv[3]
	
	url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s' % (cs1, cs2)
	req = requests.get(url, params={})
	
	jd = req.json()
	print(jd['rows'][0]['elements'][0]['distance']['text'], end="")
	print(" between", cs1, "and", cs2)
	
# -a done
if option == "-a":
	url = sys.argv[2]
	
	req = requests.get(url)
	soup = bs(req.content, 'html')
	soup.find_all('a')
	for link in soup.find_all('a'):
		print(link.get('href'))