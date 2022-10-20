from django.shortcuts import render
import requests
import requests.exceptions
import json





# Create your views here.
def homeDashBoard(request):

    s = get_ngrok_url()

    context = {
        'ngrok_url': str(s),
    }
    return render(request, 'stream/homeDashBoard.html', context)

def iotFarmView(request):
    s = get_ngrok_url()

    context = {
        'ngrok_url': str(s),
    }
    return render(request, 'stream/iotFarmView.html', context)

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

