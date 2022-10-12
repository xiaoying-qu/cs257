#!/usr/bin/env/python
# Written by Xiaoying Qu, CS257
''' 
A program that reads the Kaggle CSV files and write on CSV file for each of the tables in my databse design
'''

import csv

athletes = {}
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
            athlete_sport = row[12]
            
            if athlete_id not in athletes:
                athletes[athlete_id] = athlete_name
                writer.writerow([athlete_id, athlete_name])
            
# have a count variable

olymic_games = {}
with open('athlete_events.csv') as file,\
        open('events.csv', 'w') as olymic_games_file:
    reader = csv.reader(file)
    writer = csv.writer(olymic_games_file)
    # id, year, city, season
    next(reader)
    count = 1
    for row in reader:
        game_year = row[9]
        game_season = row[10]
        game_city = row[11]
        
        if game_year not in olymic_games and game_season not in olymic_games and game_city not in olymic_games:
            game_id = count
            writer.writerow([game_id, game_year, game_season, game_city])
            count+=1
            


events = {}
with open('athlete_events.csv') as file,\
        open('events.csv', 'w') as events_file:
    reader = csv.reader(file)
    writer = csv.writer(events_file)
    next(reader)
    count = 1
    for row in reader:
        event_name = row[13]

        if event_name not in events:
            event_id = count
            writer.writerow([event_id, event_name])
            count+=1


# a linking table named events_olympics_game so when you want to find out which athlete is at what game, the table will be helpful
