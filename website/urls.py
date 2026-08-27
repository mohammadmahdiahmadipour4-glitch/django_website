from django.contrib import admin
from django.urls import path
from .views import home , about , contact , my_profile , elements 
app_name = 'website'
urlpatterns = [
    path('' , home  , name='home') , 
    path('about' , about , name='about') , 
    path('contact' , contact , name='contact'),
    path('profile' , my_profile , name="profile_page") , 
    path('elements' , elements , name='elements' ) , 
]