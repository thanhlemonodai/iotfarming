from django.shortcuts import render, redirect
from django.views.decorators.http import condition
from django.http import StreamingHttpResponse
from farm.models import *
from farm.serializers import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.errors)
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created fro {username}!')
            return redirect('iot-home-dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'home/register.html', {'form':form})

@condition(etag_func=None)
def stream_response(request):
    resp = StreamingHttpResponse(stream_response_generator(request),
                                 content_type='text/event-stream')
    return resp



def stream_response_generator(request):
    farmstatus = FarmStatus.objects.latest("id")
    vegetable = VegetableStatus.objects.latest("id")

    vid_stream_buf_rightcam_on_1 = TestCam.objects.filter(veget=1).latest("id")
    vid_stream_buf_leftcam_on_1 = TestCam.objects.filter(veget=2).latest("id")
    vid_stream_buf_frontcam_on_1 = TestCam.objects.filter(veget=3).latest("id")
    vid_stream_buf_raspberry_cam_on_4 = TestCam.objects.filter(veget=4).latest("id")

    base64_buf_rightcam = vid_stream_buf_rightcam_on_1.frame_buf
    base64_buf_leftcam = vid_stream_buf_leftcam_on_1.frame_buf
    base64_buf_frontcam = vid_stream_buf_frontcam_on_1.frame_buf
    base64_buf_raspcam = vid_stream_buf_raspberry_cam_on_4.frame_buf

    #farm status
    temp = farmstatus.temperature
    wind = farmstatus.wind
    humidity = farmstatus.humidity
    pressure = farmstatus.pressure
    soilhumidity = int(farmstatus.water)

    print(soilhumidity)

    #vegetable status
    width = vegetable.width
    height = vegetable.high
    leaf = vegetable.leaf

    temp_string = '"temperature":"{}"'.format(temp)
    humidity_string = '"humidity":"{}"'.format(humidity)
    pressure_string = '"pressure":"{}"'.format(pressure)
    wind_string = '"wind":"{}"'.format(wind)
    soilhumidity_string = '"soilhumidity" : "{}" '.format(soilhumidity)

    base64_buf_rightcam_string = '"b64bufC01":"{}"'.format(base64_buf_rightcam)
    base64_buf_leftcam_string = '"b64bufC02":"{}"'.format(base64_buf_leftcam)
    base64_buf_frontcam_string = '"b64bufC03":"{}"'.format(base64_buf_frontcam)
    base64_buf_raspcam_string = '"b64bufC04":"{}"'.format(base64_buf_raspcam)

    string = "{" + "{}, {}, {}, {}, {}, {}, {}, {}, {}".format(temp_string,
                                                           humidity_string,
                                                           pressure_string,
                                                           wind_string,
                                                           soilhumidity_string,
                                                           base64_buf_rightcam_string,
                                                           base64_buf_leftcam_string,
                                                           base64_buf_frontcam_string,
                                                           base64_buf_raspcam_string) + "}"

    yield "data: %s\n" "retry:4000\n\n" % string

@condition(etag_func=None)
def stream_response_iotFarmView(request):
    resp = StreamingHttpResponse(stream_response_generator(request),
                                 content_type='text/event-stream')
    return resp
