from django.shortcuts import render
from django.views.decorators.http import condition
from django.http import StreamingHttpResponse
from farm.models import *
from farm.serializers import *
from asgiref.sync import sync_to_async
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
# Create your views here.

def homeview(request):
    return render(request, 'home/home.html')

def home_block(request):
    return render(request, 'home/home_block.html')

@condition(etag_func=None)
def stream_response(request):
    resp = StreamingHttpResponse(stream_response_generator(request), content_type='text/event-stream')
    return resp



def stream_response_generator(request):
    farmstatus = FarmStatus.objects.latest("id")
    vegetable = VegetableStatus.objects.latest("id")

    #farm status
    temp = farmstatus.temperature
    wind = farmstatus.wind
    humidity = farmstatus.humidity
    pressure = farmstatus.pressure

    #vegetable status
    width = vegetable.width
    height = vegetable.high
    leaf = vegetable.leaf

    temp_string = '"temperature":"{}"'.format(temp)
    humidity_string = '"humidity":"{}"'.format(humidity)
    pressure_string = '"pressure":"{}"'.format(pressure)
    wind_string = '"wind":"{}"'.format(wind)
    string = "{" + "{}, {}, {}, {}".format(temp_string, humidity_string, pressure_string, wind_string) + "}"

    yield "data: %s\n" "retry:4000\n\n" % string

@condition(etag_func=None)
def stream_response_iotFarmView(request):
    resp = StreamingHttpResponse(stream_response_generator(request), content_type='text/event-stream')
    return resp