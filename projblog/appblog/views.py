from django.shortcuts import render
from matplotlib.style import context
from requests import post



# dummy data a list comprises many dictionaries  list of posts
posts = [
    {
        'author' : 'ahmed',
        'title'  :  'blog post 1',
        'content' : 'first post content',
        'date_posted' : 'April 27, 2002'
    }, 
    {
        'author' : 'Ali',
        'title'  :  'blog post 2',
        'content' : 'Seccond post content',
        'date_posted' : 'June 27, 2022'
    }
]


# Create your views here.

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'appblog/home.html', context)

def about(request):
    return render(request, 'appblog/about.html', {'title': 'About'} )