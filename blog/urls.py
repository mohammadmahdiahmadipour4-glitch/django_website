from django.contrib import admin
from django.urls import path
from .views import blog_home , blog_single , post
app_name = 'blog'
urlpatterns = [
    path('' , blog_home  , name='blog_home') , 
    path('single' , blog_single , name='blog_single') , 
    path('posts' , post , name='test')
]