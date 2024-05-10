import requests
import json
import creds

url = "https://api-nba-v1.p.rapidapi.com/teams/statistics"

querystring = {"id":"1","season":"2021"}

headers = {
	"X-RapidAPI-Key": creds.api_key,
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())