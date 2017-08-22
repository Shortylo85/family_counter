import csv
import subprocess


with open('GeoLiteCity-Location.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')

    city_dict = {}
    for row in readCSV:
        if row[1] == 'RS':
            city_read = row[3]
            longitude_read = row[5]
            latitude_read = row[6]
#                 print("City is: {}, longitude is: {}, latitude is {}".format(city_read, longitude_read, latitude_read))

            city_dict[city_read] = [city_read,longitude_read,latitude_read]
    print(city_dict['Pancevo'])
#     print(subprocess.check_output(['pwd']))

#     if city_dict['Pancevo'][0]:
#         print(city_dict['Pancevo'][0])
#         print(city_dict['Pancevo'][1])
#         
#         print(city_dict['Pancevo'])