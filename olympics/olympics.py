'''
    olympics.py 
    Xiaoying Qu, 22 Oct 2022

    Does the following:
    Print a usage statement for "python3 olympics.py -h" (or --help). 
    List the names of all the athletes from a specified NOC.
    List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.
    
''' 
import sys
import argparse
import psycopg2
import config

def get_connection():
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file = sys.stderr)
        exit()

def get_athletes_by_noc(search_text):
    ''' Returns the names of all the athletes from a specified NOC.'''
    
    athletes = []
    try:

        query = '''SELECT DISTINCT name, abbrev
                FROM athletes, teams, event_results
                WHERE abbrev = %s
                AND event_results.athlete_id = athletes.id
                AND event_results.teams_id = teams.id
                ORDER BY name'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query,(search_text.upper(),))

        for row in cursor:
            name = row[0]
            athletes.append(name)
    
    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes

def get_medal_count_for_all():
    ''' List all the NOCs and the number of gold medals they have won, 
        in decreasing order of the number of gold medals.
    '''
    medal_count = []
    try:
        query = '''SELECT medal_count.abbrev, medal_count.gold
            FROM medal_count
            ORDER BY medal_count.gold DESC'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            noc = row[0]
            count = row[1]
            medal_count.append(f'{noc} {count}')

    except Exception as e:
        print(e, file=sys.stderr)
    
    connection.close()
    return medal_count

def get_gold_summer_2008():
    ''' List the names of all the athletes who won a gold medal
        in summer 2008.
    '''
    athletes = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = '''SELECT athletes.name, games.year, games.season
                FROM athletes, games, event_results
                WHERE year = 2008
                AND season ILIKE 'Summer%'
                AND event_results.athlete_id = athletes.id
                AND event_results.games_id = games.id
                AND event_results.medal = 'Gold'
                ORDER BY name'''
        
        cursor.execute(query)
        
        for row in cursor:
            name = row[0]
            athletes.append(name)

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes

def get_args():
    ''' get arguments '''
    parser = argparse.ArgumentParser()
    parser.add_argument('function')
    parser.add_argument('noc_search_term', nargs ="?")
    return parser.parse_args()


def main():
    args = get_args()
    if args.function == 'athletes':
        if args.noc_search_term:
            noc = args.noc_search_term
            print (f'========== Athletes from specific NOC "{noc}" ==========')
            athletes = get_athletes_by_noc(noc)
            for athlete in athletes:
                print(athlete)
            print()
    
    elif args.function == "noc_gold":
        print('========== Medal count for all NOC ==========')
        medal_count = get_medal_count_for_all()
        for count in medal_count:
            print(count)
        print()

    elif args.function == "summer_2008_gold":
        print (f'========== Athletes won gold medal in Summer 2008 ==========')
        athletes2008 = get_gold_summer_2008()
        for athlete in athletes2008:
            print(athlete)
        print()
    
    else:
        with open('usage.txt', 'r') as help_file:
            print('Usage error')
            print(help_file.read())



    

if __name__ == '__main__':
    main()