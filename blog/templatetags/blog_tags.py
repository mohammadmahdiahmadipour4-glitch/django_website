from django import template
from blog.models import Post , Category , Tag 

register = template.Library()

@register.inclusion_tag('blog/latest_post_snippet.html')
def latest_posts(count=3): 
    posts = Post.objects.filter(status=True).order_by('-published_date')[:count]

    return {'recent_posts' : posts}

@register.inclusion_tag('blog/popular_post_snippet.html')
def popular_posts(count = 3) : 
    posts = Post.objects.filter(status=True).order_by('-counted_view')[:count]

    return {'popular_posts' : posts}
@register.inclusion_tag('blog/category_widget_snippet.html')
def blog_categories():
    categories = Category.objects.all()
    return {'categories' : categories}

@register.inclusion_tag('blog/tag_widget_snippet.html')
def blog_tags() : 
    tags = Tag.objects.all()
    return {'tags' : tags}
