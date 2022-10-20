from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.homeDashBoard, name='iot-home-dashboard'),
    path('home/iotfarmview', views.iotFarmView, name='iot-farm-view'),
    path('home/projectsView', views.projectsView, name='iot-project-view'),

]