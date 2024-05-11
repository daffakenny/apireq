import requests
import json
import creds
import pandas as pd
import os
import time

def get_nbateamstats(api, team_id_list, filename):
    url = "https://api-nba-v1.p.rapidapi.com/teams/statistics"
    all_teams_stats = []
    
    for team_id in team_id_list: # For loop to query each team's stats manually
        
        # Stage 1 = Pre-Season, 2 = Regular Season, 3 = Playoffs?
        querystring = {"id": team_id, "season": "2021", "stage" : 2}

        headers = {
            "X-RapidAPI-Key": api,
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
            }

        response = requests.get(url, headers=headers, params=querystring)
        print("Team ID:", team_id, "Response:", response.json())

        api_data = response.json()
        
        # Selects which data from API to be included in JSON
        team_stats = {
            "id": api_data["parameters"]["id"], # Include TeamID
            "response": api_data["response"] # General team stats per TeamID
        }
        all_teams_stats.append(team_stats)

        time.sleep(6)  # 6 secs delay

    with open(filename, "w") as file:
        json.dump(all_teams_stats, file, indent = 4)            

def get_json2csv(filename,team_id_list) :
    with open(filename, 'r') as json_data:
        data = json.load(json_data)
        output_filename = os.path.splitext(filename)[0] # [0] returns base filename without its  extension
        combined_df = pd.DataFrame()  # Initialize combined_df name
        
        for team_id in team_id_list:
            for entry in data:
                if entry["id"] == str(team_id): # Using string since JSON return is string-based 
                    response_data = entry["response"]
                    df = pd.json_normalize(response_data) # Insert "response" as the dataset by Pandas
                    df.insert(0, "teamID", team_id ) # Insert teamID as the first column for csv
                    combined_df = pd.concat([combined_df, df], ignore_index=True)
                    
                    break

        print("Combined DataFrame:", combined_df)
        combined_df.to_csv(output_filename+"_normalized.csv", index=False)

api = creds.api_key
filename = 'nbateamstats.json'

team_id_list = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 38, 40, 41]
get_nbateamstats(api, team_id_list, filename)
get_json2csv(filename, team_id_list)