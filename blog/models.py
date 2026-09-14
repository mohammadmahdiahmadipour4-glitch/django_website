from django.db import models

# Create your models here.
class User(models.Model) : 
    username = models.CharField(max_length=80 , unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120) 
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    superuser = models.BooleanField(default=False)
    staff = models.BooleanField(default=False) 

    def __str__(self):
        return self.username 

    
class Tag(models.Model) : 
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120 , default='notset')
    def __str__(self):
        return self.name

class Post(models.Model): 
    author = models.OneToOneField(to=User , on_delete= models.CASCADE ,)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/')
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.CharField(max_length=80)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True , blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(to=Tag)
    category = models.ForeignKey(to= Category , on_delete=models.SET_NULL , blank=True , null=True)

    def __str__(self):
        return self.title

class contact(models.Model):
    name = models.CharField(max_length=300)
    subject = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
