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
        for row in reader:
            athlete_id = row[0]
        
            athlete_name = row[1]
      
        if athlete_id not in athletes:
            athletes[athlete_id] = athlete_name
            writer.writerow([athlete_id, athlete_name])

olymic_games = {}
with open('athlete_events.csv') as file,\
        open('events.csv', 'w') as olymic_games_file:
    reader = csv.reader(file)
    writer = csv.writer(olymic_games_file)
    for row in reader:
            athlete_id = row[0]
        
            athlete_name = row[1]
      
        if athlete_id not in athletes:
            athletes[athlete_id] = athlete_name
            writer.writerow([athlete_id, athlete_name])



events = {}
with open('athlete_events.csv') as file,\
        open('events.csv', 'w') as events_file:
    reader = csv.reader(file)
    writer = csv.writer(events_file)
        