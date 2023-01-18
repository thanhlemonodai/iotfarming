from datetime import datetime, timedelta

from django.shortcuts import render
import requests
import requests.exceptions
import json
from django.views.decorators.csrf import csrf_exempt
from farm.models import *
from farm.serializers import *



@csrf_exempt
def homeDashBoard(request):
    s = get_ngrok_url()

    context = {
        'ngrok_url': str(s),

    }
    return render(request, 'stream/homeDashBoard.html', context)

@csrf_exempt
def iotFarmView(request):
    date_list = []
    dt = datetime.now()
    range_date = 20
    for i in range(range_date):
        preday = dt - timedelta(range_date - i)
        date_list.append(preday.date().__str__())
    print(date_list)
    temperature_list = []
    water_list = []
    humidity_list = []
    for j in range(len(date_list)):
        farmstatus = FarmStatus.objects.filter(
            datetimeonfarm__range=["{} 20:40:00".format(date_list[j]), "{} 20:46:00".format(date_list[j])])
        try:
            temperature_list.append(farmstatus[0].temperature)
            water_list.append(((1150-(farmstatus[0].water//10000))/1150)*100)
            humidity_list.append(farmstatus[0].humidity)
        except IndexError as e:
            pass
    print(temperature_list)
    print(humidity_list)
    print(water_list)
    s = get_ngrok_url()

    context = {
        'ngrok_url': str(s),
        'temp_chart': temperature_list,
        'water_chart': water_list,
        'humidity_chart': humidity_list,
    }
    data = json.dumps(context)
    return render(request, 'stream/iotFarmView.html', {'data':data})

def projectsView(request):

    return render(request, 'stream/projects.html')

def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels/"
    try:
        res = requests.get(url)
        res_unicode = res.content.decode("utf-8")
        res_json = json.loads(res_unicode)
        for i in res_json["tunnels"]:
            if i['name'] == 'command_line':
                return i['public_url']
    except requests.ConnectionError as e:
        pass

    return ""

