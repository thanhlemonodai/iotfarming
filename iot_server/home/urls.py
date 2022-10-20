from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('home/view', views.home_block, name='home_block'),
path('stream/senddata', views.stream_response, name='stream-response'),

]