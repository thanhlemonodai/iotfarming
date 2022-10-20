from django.db import models
from django.utils import timezone

# Create your models here.
class FarmInformation(models.Model):
    farm_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    message = models.TextField()
    gps = models.CharField(max_length=50)

    def __str__(self):
        return "{}:{}".format(self.pk, self.farm_name)

class FarmStatus(models.Model):
    temperature = models.FloatField() #温度
    humidity = models.FloatField()    #湿度
    wind = models.FloatField()        #風
    pressure = models.FloatField()    #圧力
    water = models.FloatField()       #水量
    datetimeonfarm = models.DateTimeField()
    farminfo = models.ForeignKey(FarmInformation,
                                 blank=True,
                                 null=True,
                                 related_name="farmstatus",
                                 on_delete=models.CASCADE)

    def __str__(self):
        return "{} :{}".format(self.pk, self.datetimeonfarm)

class Vegetable(models.Model):
    vegetablename = models.CharField(max_length=20)
    season = models.CharField(max_length=40)
    qualiative = models.TextField()

    def __str__(self):
        return "{}".format(self.vegetablename)

class VegetableStatus(models.Model):
    high = models.FloatField()  # 高さ
    width = models.FloatField()  # 幅
    leaf = models.BooleanField(default=True)
    datetimegrowth = models.DateTimeField()
    image = models.FileField(upload_to='veget_pic', default='veget_pic/1.png')
    vegetable = models.ForeignKey(Vegetable,
                                  blank=True,
                                  null=True,
                                  related_name="vegetable",
                                  on_delete=models.CASCADE)
    def __str__(self):
        return "{}:{}".format(self.vegetable.vegetablename, self.datetimegrowth)

class ControlButtonInFarm(models.Model):
    pomp1 = models.BooleanField(null=False)
    pomp2 = models.BooleanField(null=False)
    servor1 = models.BooleanField(null=False)
    servor2 = models.BooleanField(null=False)
    fan1 = models.BooleanField(null=False)
    fan2 = models.BooleanField(null=False)
    saveEnergy = models.BooleanField(null=False)
    test_fields = models.BooleanField(null=False)


class VegetableTimeLapseVideo(models.Model):
    growth_video = models.FileField()   #ミニトマトの生長の管理ビデオ

