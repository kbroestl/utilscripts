#! /usr/bin/env python

import os
from dotenv import load_dotenv
import threading
import requests
import json
from scipy.constants import convert_temperature

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')
URL = "https://api.openweathermap.org/data/2.5/weather?zip="

def fetch_function(value):
	'''
	Takes a location code (zip/PLZ+country) and fetches json data from the API
	Service.
	Full return has a structure like this:
	{
	"coord":
		{"lon":-83.2853,"lat":39.9424},
	"weather":
		[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
	"base":"stations",
	"main":
		{
		"temp":277.96,
		"feels_like":273.17,
		"temp_min":276.91,
		"temp_max":279.09,
		"pressure":1012,
		"humidity":77
		},
	"visibility":10000,
	"wind":
		{
		"speed":7.72,
		"deg":270,
		"gust":11.32
		},
	"clouds":
		{
		"all":100
		},
	"dt":1666127324,
	"sys":
		{
		"type":2,
		"id":2007036,
		"country":"US",
		"sunrise":1666093591,
		"sunset":1666133382
		},
	"timezone":-14400,
	"id":0,
	"name":"West Jefferson",
	"cod":200
	}

	'''

	to_fetch = "{url}{zip}&appid={key}".format(url=URL, zip=value, key=API_KEY)
	
	response = requests.get(to_fetch)

	format_data(json.loads(response.text))

def format_data(jsondata):
	'''
	We're only interested in a few elements from that massive bit o' json so
	fold/spindle/mutilate as necessary.
	'''
	current_temp = convert_temperature([jsondata['main']['temp']], 'K', 'F')
	loc_name = jsondata['name']
	current_cond = jsondata['weather'][0]['main']

	print("Conditions at {place}: {temp} with {h}% humidity and {conditions}".format( \
		place = loc_name,
		temp = "{:3.1f}F".format(current_temp[0]),
		conditions = current_cond,
        h = jsondata['main']['humidity'] ))


if __name__ == "__main__":
	threads = list()
	for index,value in enumerate(["43162,us","80513,us","49931,us","26135,de","V6L,ca"]):
		x = threading.Thread(target=fetch_function, args=(value,))
		threads.append(x)
		x.start()

