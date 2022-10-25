from importlib.resources import path
from django.urls import URLPattern
from django.urls import path
from django.contrib import admin
from .import views

from django.urls import path , include


urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='blog-about'),
] 