from django.contrib import admin
# admin webpage pe model show krwany k liya 1stly model import than register
from .models import post
# Register your models here.
admin.site.register(post)