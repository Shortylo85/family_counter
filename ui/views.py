import csv

from django.shortcuts import render, redirect
from .forms import RegistrationForm

def index(request):
    return render(request, template_name="ui/index.html")

def register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('index')
    else:
        register_form = RegistrationForm()
    
    built_context = {'form':register_form}
        
    return render(request, template_name='account/register.html', context=built_context)

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
    
                city_dict[city_read] = [longitude_read,latitude_read,city_read]
       
    
        if city_dict['Omoljica']:
            print(city_dict['Omoljica'][0])
            print(city_dict['Omoljica'][1])
            print(city_dict['Omoljica'][2])
        
        latitude = city_dict['Omoljica'][0]
        longitude = city_dict['Omoljica'][1]
        city_name = city_dict['Omoljica'][2]
#     ip = requests.get('https://api.ipify.org').text
#     loc_string = requests.get('https://ipapi.co/{}/json/'.format(ip))
#     loc = loc_string.text
#     loc_json = json.loads(loc)
#     longitude = loc_json['longitude']
#     latitude = loc_json['latitude']
    
    built_context = {
                'lon':longitude,
                'lat':latitude,
                'city':city_name,
                'user': request.user
    }
    
    print(built_context)
    return render(request, template_name="ui/map.html", context = built_context)
