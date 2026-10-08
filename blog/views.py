from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post , Comment
from django.db.models import Q
from django.core.paginator import Paginator


def blog_home(request , cat_name = None , tag_name = None) : 
    posts = Post.objects.filter(status = True)

    paginator = Paginator(posts , 4 )

    page_number = request.Get.get('page')

    posts = paginator.get_page(page_number) 
    
    if cat_name : 
        posts = posts.filter(category__name = cat_name)

    if tag_name:
        posts = posts.filter(tag__name = tag_name)
    context = {
        'posts' : posts , 
    }

    return render(request , 'blog/blog-home.html' , context)





def blog_single(request , post_id) :
    post = get_object_or_404(Post , id= post_id , status = True)
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()

    comments = Comment.objects.filter(post= post , is_approved = True)

    if request.method == 'POST':
        c_name = request.POST.get('name')
        c_email = request.POST.get('email')
        c_subject = request.POST.get('subject')
        c_message = request.POST.get('message')

        Comment.objects.create(
            post = post , 
            name = c_name , 
            email = c_email,
            subject = c_subject , 
            message = c_message
        )

        return redirect('blog:blog_single', post_id=post.id)
    context = {
        'post' : post , 
        'next_post' : next_post , 
        'prev_post': prev_post,
        'comments': comments  , 
    }
    return render(request , 'blog/blog-single.html' , context )

def blog_search(request) : 
    posts = Post.objects.filter(status = True )

    if request.method == 'GET' : 
        query = request.GET.get('search')
        if query : 
            posts = posts.filter(Q(title__icontains=query) | Q(content__icontains = query))

        context = {'posts' : posts}

        return render(request , 'blog/blog-home.html' , context )