from django.urls import path
from .views import blog_home , blog_single , blog_search
app_name = 'blog'
urlpatterns = [
    path('' , blog_home  , name='blog_home') , 
    path('single/<int:post_id>/' , blog_single , name='blog_single') , 
    path('categroy/<str:cat_name>/' , blog_home , name='blog_category'),
    path('tag/<str:tag_name>/', blog_home , name='blog_tag'),
    path('search/', blog_search , name='blog_search' )
    
]