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

@api.route('/fuel_consumption/') 
def get_car_fuel ():
    query = '''SELECT modeltable.model, modeltable.make, fueltable.consumption_comb
                FROM modeltable, fueltable, linkstable
                WHERE modeltable.id = linkstable.modelID
                AND fueltable.id = linkstable.modelID
                ORDER BY fueltable.consumption_comb DESC
                LIMIT 20; '''
    car_fuel_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor() 
        cursor.execute(query)
        print(cursor.query)
        for row in cursor:
            car = {'model':row[0],
                      'make':row[1],
                      'fuel_consumption':row[2]}
            car_fuel_list.append(car)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(car_fuel_list)

@api.route('/co2/') 
def get_car_co2 ():
    query = '''SELECT * FROM co2table '''
    car_co2_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor() 
        cursor.execute(query)
        print(cursor.query)
        for row in cursor:
            people = {'id':row[0],
                      'emission':row[1],
                      'c_rating':row[2],
                      's_rating':row[3]}
            car_co2_list.append(people)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(car_co2_list)

@api.route('/search/<make>')
def search_cars_for_make(make):
    query = '''SELECT modeltable.model, modeltable.make, fueltable.consumption_comb
                FROM modeltable, fueltable, linkstable
                WHERE modeltable.make ILIKE CONCAT('%%', %s, '%%')
                AND modeltable.id = linkstable.modelID
                AND fueltable.id = linkstable.fuelID
                LIMIT 10;'''
    car_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (make,))
        for row in cursor:
            car = {'model':row[0], 'make':row[1], 'co2':row[2]}
            car_list.append(car)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(car_list)