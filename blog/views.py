from django.shortcuts import render
from .models import Post
def blog_home(request) : 
    return render(request , 'blog/blog-home.html')

def blog_single(request) : 
    return render(request , 'blog/blog-single.html')

def post(request) : 
    posts = Post.objects.all()
    content = {
        'posts' : posts , 
    }
    return render(request , 'blog/posts.html' , content)