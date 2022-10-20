from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(FarmStatus)
admin.site.register(Vegetable)
admin.site.register(VegetableStatus)
#admin.site.register(VegetableTimeLapseVideo)
admin.site.register(FarmInformation)
admin.site.register(ControlButtonInFarm)