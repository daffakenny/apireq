import requests
import json
import creds
import pandas as pd
import os

def get_nba_standings(api, filename):
	url = "https://api-nba-v1.p.rapidapi.com/standings"

	querystring = {"league":"standard","season":"2021"}

	headers = {
		"X-RapidAPI-Key": api,
		"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	print(response.json())
	api_data = response.json()

	with open(filename, "w") as file:
		json.dump(api_data, file, indent=4)

def get_json2csv(filename) :
    with open(filename, 'r') as json_data:
        data = json.load(json_data)
        df = pd.json_normalize(data['response']) # Change response to the last Array of the desired data, see check each ".JSON" for reference
        
        output_filename = os.path.splitext(filename)[0] # [0] -> Return base filename without its  extension
        df.to_csv(output_filename + '_normalized.csv')

api = creds.api_key
filename = 'nbastandings.json'
get_nba_standings(api, filename)
get_json2csv(filename)