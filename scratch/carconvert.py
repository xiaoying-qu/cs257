'''
    Convert.py

    Converts the 2022_rating.csv to csv

    Written by Yiming Xia and Xiaoying Qu

'''

import csv

model_table = {}
fuel_table= {}
co2_table = {}


with open ('2022_ratings.csv') as input_file,\
    open('car_data.csv','w') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    next(reader)
    
    for row in reader:
        make = row[1]
        model = row[2]
        vehicle_class = row[3]
        engine = row[4]
        cylinder_size = row[5]

        key = (make,model,vehicle_class,engine,cylinder_size)
        if key not in model_table:
            model_table[key] = len(model_table) + 1
        model_table_id = model_table[key]

        fuel_type = row[7]
        con_city = row[8]
        con_hwy = row[9]
        con_comb = row[10]

        key = (fuel_type,con_city,con_hwy,con_comb)
        if key not in fuel_table:
            fuel_table[key] = len(fuel_table) + 1
        fuel_table_id = fuel_table[key]

        c_emission = row[11]
        c_rating = row[12]
        smog_rating = row[13]
        key = (c_emission,c_rating,smog_rating)
        if key not in co2_table:
            co2_table[key] = len(co2_table) + 1
        co2_table_id = co2_table[key]

   
        writer.writerow([model_table_id,fuel_table_id,co2_table_id])


with open('modelTable.csv','w') as modelTable_file:
    writer = csv.writer(modelTable_file)
    for (make,model,vehicle_class,engine,cylinder_size) in model_table:
        model_table_id = model_table[((make,model,vehicle_class,engine,cylinder_size))]
        writer.writerow([model_table_id,make,model,vehicle_class,engine,cylinder_size])


with open('fuelTable.csv','w') as fuelTable_file:
    writer = csv.writer(fuelTable_file)
    for (fuel_type,con_city,con_hwy,con_comb) in fuel_table:
        fuel_table_id = fuel_table[(fuel_type,con_city,con_hwy,con_comb)]
        writer.writerow([fuel_table_id,fuel_type,con_city,con_hwy,con_comb])

with open('co2Table.csv','w') as co2Table_file:
    writer = csv.writer(co2Table_file)
    for (c_emission,c_rating,smog_rating) in co2_table:
        co2_table_id = co2_table[(c_emission,c_rating,smog_rating)]
        writer.writerow([co2_table_id,c_emission,c_rating,smog_rating])

    