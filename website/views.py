from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
def home(request) :
    return render(request , 'website/index.html')

def about(request) : 
    return render(request  , 'website/about.html')

def contact(request) : 
    return render(request , 'website/contact.html')

def my_profile(request) : 
    user_data = {
        'name' : "mohammad" , 
        'last_name' : "ahmadi" , 
        'uni' : 'sutech' , 
        'is_admin' : False , 
        'skills' : ['python' , 'django' , 'telegram_bots']
    }

    return render(request=request , template_name='profile.html' , context=user_data)

def elements(request) : 
    return render(request , 'website/elements.html')