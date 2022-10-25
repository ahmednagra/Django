from importlib.resources import path
from django.urls import URLPattern
from django.urls import path
from django.contrib import admin
from .import views


urlpatterns = [
 path("index", views.index),
 path("home", views.home)
] 