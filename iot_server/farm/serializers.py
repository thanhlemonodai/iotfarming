from rest_framework import serializers
from .models import *

class FarmStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = FarmStatus
        fields = ('id', 'temperature', 'humidity', 'wind', 'pressure', 'water', 'datetimeonfarm', 'farminfo')


class FarmInformationSerializers(serializers.ModelSerializer):
    farmstatus = FarmStatusSerializers(many=True)
    class Meta:
        model = FarmInformation
        fields = ('id', 'farm_name', 'address', 'message', 'gps', 'farmstatus')

class VegetableStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = VegetableStatus
        fields = ('id', 'high', 'width', 'leaf', 'datetimegrowth', 'image', 'vegetable')

class VegetableSerializers(serializers.ModelSerializer):
    vegetable = VegetableStatusSerializers(many=True)
    class Meta:
        model = Vegetable
        fields = ('id', 'vegetablename', 'season', 'qualiative', 'vegetable')

class VegetableTimeLapseVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = VegetableTimeLapseVideo
        fields = ('growth_video')


class ControlButtonInFarmSerializers(serializers.ModelSerializer):
    class Meta:
        model = ControlButtonInFarm
        fields = "__all__"

class TestCamSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestCam
        fields = "__all__"