import csv
import json
import subprocess

from django.shortcuts import render
import requests


# Create your views here.
def index(request):

    return render(request, template_name="ui/index.html")

def getMap(request):
    
#     print(subprocess.check_output(['pwd']))
    

    with open('/home/danijel/family_counter/family_counter/ui/GeoLiteCity-Location.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
    
        city_dict = {}
        for row in readCSV:
            if row[1] == 'RS':
                city_read = row[3]
                longitude_read = row[5]
                latitude_read = row[6]
    #                 print("City is: {}, longitude is: {}, latitude is {}".format(city_read, longitude_read, latitude_read))
    
                city_dict[city_read] = [longitude_read,latitude_read]
       
    
        if city_dict['Djakovica']:
            print(city_dict['Djakovica'][0])
            print(city_dict['Djakovica'][1])
            print(city_dict['Djakovica'])
        
        latitude = city_dict['Djakovica'][0]
        longitude = city_dict['Djakovica'][1]
#     ip = requests.get('https://api.ipify.org').text
#     loc_string = requests.get('https://ipapi.co/{}/json/'.format(ip))
#     loc = loc_string.text
#     loc_json = json.loads(loc)
#     longitude = loc_json['longitude']
#     latitude = loc_json['latitude']
    
    built_context = {
                'lon':longitude,
                'lat':latitude,
#                 'city':city,
    }
    
    print(built_context)
    return render(request, template_name="ui/map.html", context = built_context)
