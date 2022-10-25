from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from requests import Response
from django.contrib import staticfiles
# Create your views here.
def index(request):
    return HttpResponse("This is Index Function")


def home(request):
   return render(request, "portfolio/home.html")
   