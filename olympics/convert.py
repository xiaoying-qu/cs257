#!/usr/bin/env/python
# Written by Xiaoying Qu, CS257
''' 
A program that reads the Kaggle CSV files and write on CSV file for each of the tables in my databse design
'''

import csv
from itertools import zip_longest


athletes = {}
athletes_info=[]
with open('athlete_events.csv','r') as file,\
        open('athletes.csv', 'w') as athletes_file:
        reader = csv.reader(file)
        writer = csv.writer(athletes_file)
        # skip the header
        next(reader)
        for row in reader:
            athlete_id = row[0]
            athlete_name = row[1]
            athlete_sex = row[2]
            athlete_age = 0 if 'NA' == row[3] else round(float(row[3]))
            athlete_height = 0 if 'NA'== row[4] else round(float(row[4]))
            athlete_weight = 0 if 'NA'== row[5] else round(float(row[5]))
            events_name = row[13]
            events_name = events_name.replace(',','')
            athlete_sport = row[12]
          
            #l= []
            if athlete_id not in athletes:
                athletes[athlete_id] = athlete_name
                #l=[athlete_id, athlete_name, athlete_sex, athlete_age, athlete_height,
                    #athlete_weight, athlete_sport]
                writer.writerow([athlete_id, athlete_name, athlete_sex, athlete_age, athlete_height,
                    athlete_weight, athlete_sport])

            #medals = f"{row[8]}{events_name} {row[14]}"
            #l+=[medals]
            #athletes_info.append(l)
            #for item in athletes_info:
            
        
         
# have a count variable

olymic_games = {}
olymic_games = set()
with open('athlete_events.csv') as file,\
        open('olympic_games.csv', 'w') as olymic_games_file:
    reader = csv.reader(file)
    writer = csv.writer(olymic_games_file)
    # id, year, city, season
    next(reader)
    count = 1
    for row in reader:
        game = row[8]
        game_year = row[9]
        game_season = row[10]
        game_city = row[11]
        
        if game not in olymic_games:
            game_id = count
            olymic_games.add(game)
            olymic_games.add(game_year)
            olymic_games.add(game_season)
            olymic_games.add(game_city)
            writer.writerow([game_id, game, game_year, game_season, game_city])
            count+=1
            
            


events = {}
# create an events set 
events = set()
with open('athlete_events.csv') as file,\
        open('events.csv', 'w') as events_file:
    reader = csv.reader(file)
    writer = csv.writer(events_file)
    next(reader)
    count = 1
    for row in reader:
        events_name = row[13]
        events_name = events_name.replace(',','')

        if events_name not in events:
            events_id = count
            events.add(events_name)
            writer.writerow([events_id, events_name])
            count+=1

teams = {}
teams = set()
with open('athlete_events.csv') as file,\
        open('teams.csv', 'w') as teams_file:
    reader = csv.reader(file)
    writer = csv.writer(teams_file)
    next(reader)
    count = 1
    for row in reader:
        team = row[6]
        noc = row[7]
        if team not in teams:
            team_id = count
            teams.add(team)
            teams.add(noc)
            writer.writerow([team_id,team,noc])
            count+=1

medals = {}
medals = set()
with open('athlete_events.csv') as file,\
        open('medals.csv', 'w') as teams_file:
    reader = csv.reader(file)
    writer = csv.writer(teams_file)
    next(reader)
    count = 1
    for row in reader:
        if row[14] != 'NA':
            medal_id = count
            medals.add(medal_id)
            medal = row[14]
            medals.add(medal)
            game = row[8]
            medals.add(game)
            owner = row[1]
            medals.add(owner)
            team = row[6]
            medals.add(team)
            event = row[13]
            medals.add(event)
            writer.writerow([medal_id,medal,game,owner,team,event])
            count+=1

            

        
        


