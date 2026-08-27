from django.contrib import admin
from django.urls import path
from .views import blog_home , blog_single
app_name = 'blog'
urlpatterns = [
    path('' , blog_home  , name='blog_home') , 
    path('single' , blog_single , name='blog_single') , 
    
]