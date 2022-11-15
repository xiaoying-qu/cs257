# CS257 end-to-end assignment
# written by Xiaoying QU and Yiming Xia
# 11.9.2022


import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password)

@api.route('/people/') 
def get_people ():
    query = '''SELECT * FROM people '''
    people_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor() 
        cursor.execute(query)
        print(cursor.query)
        for row in cursor:
            people = {'id':row[0],
                      'name':row[1],
                      'age':row[2]}
            people_list.append(people)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(people_list)

