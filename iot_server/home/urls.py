from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('home/view', views.home_block, name='home_block'),
    path('stream/senddata', views.stream_response, name='stream-response'),

    path('login/', auth_views.LoginView.as_view(template_name = 'home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'home/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

]