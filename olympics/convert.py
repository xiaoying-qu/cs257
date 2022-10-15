#!/usr/bin/env/python
# Written by Xiaoying Qu, CS257
''' 
A program that reads the Kaggle CSV files and write on CSV file for each of the tables in my databse design
'''

import csv

athletes = {} # maps (name, sex) --> id
games = {} # maps (city, year, season) --> integer id
teams = {} #maps (country, abbrev) --> id
sports = {} #maps (sport) --> id
events = {} #maps (event) --> id

with open('athlete_events.csv') as input_file,\
        open('event_results.csv', 'w') as event_results_file:
    reader = csv.reader(input_file)
    next(reader)
    event_results_writer = csv.writer(event_results_file)
    for row in reader:
        athlete_id = row[0]
        athlete_name = row[1]
        athlete_sex = row[2]
        key = (athlete_name, athlete_sex)
        if key not in athletes:
            athletes[key] = athlete_id
    
        country = row[6]
        abbrev = row[7]
        key = (country, abbrev)
        if key not in teams:
            teams[key] = len(teams) + 1
        teams_id = teams[key]

        year = row[9]
        season = row[10]
        city = row[11]
        key = (city, year, season)
        if key not in games:
            games[key] = len(games) + 1
        games_id = games[key]

        sport = row[12]
        key = sport
        if key not in sports:
            sports[key] = len(sports) + 1
        sports_id = sports[key]
        
        event = row[13]
        event = event.replace(',','')
        key = event
        if key not in events:
            events[key] = len(events) + 1
        events_id = events[key]
    
        medal = row[14]

        
        # HERE: we have in hand an athlete_id and a games_id
        # so we could write to the event_results csv.writer
        athlete_age = row[3]
        athlete_age = 0 if athlete_age == 'NA' else int(round(float(athlete_age)))
        athlete_height = row[4]
        athlete_height = 0 if row[4] == 'NA' else int(round(float(row[4])))
        athlete_weight = row[5]
        athlete_weight = 0 if row[5] == 'NA' else int(round(float(row[5])))
        event_results_writer.writerow([athlete_id, athlete_age, athlete_height,\
        athlete_weight,games_id, teams_id, events_id, sports_id, medal])

        
with open('athletes.csv','w') as athletes_file:
    writer = csv.writer(athletes_file)
    for (athlete_name, athlete_sex) in athletes:
        athletes_id = athletes[(athlete_name,athlete_sex)]
        writer.writerow([athletes_id,athlete_name,athlete_sex])

with open('games.csv', 'w') as games_file:
    writer = csv.writer(games_file)
    for (city, year, season) in games:
        games_id = games[(city, year, season)]
        writer.writerow([games_id, city, year, season])

with open('teams.csv', 'w') as teams_file:
    writer = csv.writer(teams_file)
    for (country, abbrev ) in teams:
        teams_id = teams[(country, abbrev)]
        writer.writerow([teams_id,country,abbrev])
        
with open('sports.csv','w') as sports_file:
    writer = csv.writer(sports_file) 
    for (sport) in sports:
        sports_id =sports[sport] 
        writer.writerow([sports_id,sport])
       

with open('events.csv','w') as events_file:
    writer = csv.writer(events_file)
    for (event) in events:
        events_id = events[event]     
        writer.writerow([events_id,event])    
