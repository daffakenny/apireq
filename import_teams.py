import requests
import json
import creds

url = "https://api-nba-v1.p.rapidapi.com/teams"

headers = {
	"X-RapidAPI-Key": creds.api_key,
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
print(response.json())
api_data = response.json()

with open("nbateams.json", "w") as file:
    json.dump(api_data, file, indent=4)