from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # UserPassesTestMixin se sirf author he post update ya edit kr skta hia
# ab post ko listview daikhny k liya
from django.views.generic import (
    ListView,
     DetailView,
     CreateView,
     UpdateView, 
     DeleteView )
from matplotlib.pyplot import cla
from .models import post

# dummy data a list comprises many dictionaries  list of posts
postsss = [
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
        # is query se post model ki timam valus fetch ho jian ge post moodel jo models mein define kiya gaya hai
        'posts' : post.objects.all()
    }
    return render(request, 'appblog/home.html', context)

class PostListView(ListView):
    model = post
    template_name = 'appblog/home.html'   
    context_object_name = 'posts'
    ordering = ['-date_posted']  # ( - ) se ab date lastest oper aur older neachy 

class PostDetailView(DetailView):
    model = post

class PostCreateView(LoginRequiredMixin, CreateView): # just mention the fields that we required in form
    model = post    
    fields = ['title', 'content']

    def form_valid(self, form):  # automatically author ki id post se link ho join ge
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView): # just mention the fields that we required in form
    model = post    
    fields = ['title', 'content']

    def form_valid(self, form):  # automatically author ki id post se link ho join ge
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
            
def about(request):
    return render(request, 'appblog/about.html', {'title': 'About'} )