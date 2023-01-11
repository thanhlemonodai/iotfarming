from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
###############################################
#farm_status_view
@csrf_exempt
def farm_status_view_all(request):
    try:
        farmstatus = FarmStatus.objects.all()
        if farmstatus.exists():
            return render(request, 'farm/farm_status_view_all.html', {'farmstatus': farmstatus})
    except FarmStatus.DoesNotExist:
        raise Http404("data does not exist")
    return render(request, 'farm/farm_status_view_all.html')
@csrf_exempt
def farm_information_view(request):
    try:
        farminfos = FarmInformation.objects.all()
        farmstatus = FarmStatus.objects.all()
    except FarmInformation.DoesNotExist:
        raise Http404("data does not exist")
    return render(request, 'farm/farm_information_view.html', {'farminfos':farminfos,
                                                               'farmstatus':farmstatus})

###############################################
#vegetable_status_view
@csrf_exempt
def vegetable_status_view(request):
    try:
        vegetablestatus = VegetableStatus.objects.all()
    except VegetableStatus.DoesNotExist:
        raise Http404("data does not exist")
    return render(request, 'farm/vegetable_status_view_all.html', {'vegetablestatus':vegetablestatus})
@csrf_exempt
def vegetable_view(request):
    try:
        vegetable = Vegetable.objects.all()
    except Vegetable.DoesNotExist:
        raise Http404("data does not exist")
    return render(request, 'farm/vegetable_view.html', {'vegetables':vegetable})

###############################################
#set API of farm status
@api_view(['GET'])
@csrf_exempt
def api_farm_status_list(request):
    farm_status = FarmStatus.objects.all()
    serializers = FarmStatusSerializers(farm_status, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@csrf_exempt
def api_farm_status_detail(request, pk):
    farm_status = FarmStatus.objects.get(id=pk)
    serializers = FarmStatusSerializers(farm_status, many=False)
    return Response(serializers.data)

@csrf_exempt
@api_view(['POST', 'GET'])
def api_farm_status_create(request):
    serializers = FarmStatusSerializers(data=request.data)

    if serializers.is_valid():
        serializers.save()
    else:
        print(serializers.errors)
    return Response(serializers.data)

@api_view(['POST'])
@csrf_exempt
def api_farm_status_update(request, pk):
    farm_status = FarmStatus.objects.get(id=pk)
    serializers = FarmStatusSerializers(instance=farm_status,
                                        data=request.data)
    if serializers.is_valid():
        serializers.save()
    else:
        print(serializers.errors)
    return Response(serializers.data)

###############################################
#set API of Farm's information
@api_view(['GET'])
@csrf_exempt
def api_farm_info_list(request):
    farm_info = FarmInformation.objects.all()
    serializers = FarmInformationSerializers(farm_info, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@csrf_exempt
def api_farm_info_detail(request, pk):
    farm_info = FarmInformation.objects.get(id=pk)
    serializers = FarmInformationSerializers(farm_info, many=False)
    return Response(serializers.data)

@api_view(['POST', 'GET'])
@csrf_exempt
def api_farm_info_create(request):
    serializers = FarmInformationSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
@csrf_exempt
def api_farm_info_update(request, pk):
    farm_info = FarmInformation.objects.get(id=pk)
    serializers = FarmInformationSerializers(instance=farm_info,
                                        data=request.data)
    if serializers.is_valid():
        serializers.save()
    else:
        print(serializers.errors)
    return Response(serializers.data)

###############################################
#Set API of vegetable's information
@api_view(['GET'])
@csrf_exempt
def api_vegetable_list(request):
    vegetable = Vegetable.objects.all()
    serializers = VegetableSerializers(vegetable, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@csrf_exempt
def api_vegetable_detail(request, pk):
    vegetable = Vegetable.objects.get(id=pk)
    serializers = VegetableSerializers(vegetable, many=False)
    return Response(serializers.data)

@api_view(['POST', 'GET'])
@csrf_exempt
def api_vegetable_post(request):
    serializers = VegetableSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST', 'GET'])
@csrf_exempt
def api_vegetable_update(request, pk):
    vegetable = Vegetable.objects.get(id=pk)
    serializers = VegetableSerializers(instance=vegetable,
                                       data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

###############################################
#set vegetable info and status
@api_view(['GET'])
@csrf_exempt
def api_vegetable_status_list(request):
    vegetablestatus = VegetableStatus.objects.all()
    serializers = VegetableStatusSerializers(vegetablestatus, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@csrf_exempt
def api_vegetable_status_detail(request, pk):
    vegetablestatus = VegetableStatus.objects.get(id=pk)
    serializers = VegetableStatusSerializers(vegetablestatus, many=False)
    return Response(serializers.data)

@api_view(['POST', 'GET'])
@csrf_exempt
def api_vegetable_status_post(request):
    serializers = VegetableStatusSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST', 'GET'])
@csrf_exempt
def api_vegetable_status_update(request, pk):
    vegetable = VegetableStatus.objects.get(id=pk)
    serializers = VegetableStatusSerializers(instance=vegetable,
                                       data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@csrf_exempt
def farm_view(request):
    return render(request, 'farm/farm.html')


@api_view(['POST', 'GET'])
@csrf_exempt
def cam_model_crate(request):
    serializers = TestCamSerializers(data = request.data)

    if serializers.is_valid():
        print(serializers.errors)
        serializers.save()
    return Response(serializers.data)

@api_view(['POST','GET'])
@csrf_exempt
def control_button_farm_update(request, pk):
    controlButton = ControlButtonInFarm.objects.get(id=pk)
    serializers = ControlButtonInFarmSerializers(instance=controlButton,
                                                 data=request.data)

    if serializers.is_valid():
        print(serializers.errors)
        serializers.save()
    return Response(serializers.data)

@api_view(['GET'])
@csrf_exempt
def control_button_farm_view(request, pk):
    controlButton = ControlButtonInFarm.objects.get(id=pk)
    serializers = ControlButtonInFarmSerializers(controlButton, many=False)
    return Response(serializers.data)
