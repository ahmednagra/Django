from email.policy import default
from unittest.util import _MAX_LENGTH
from certifi import contents
from django.db import models
from matplotlib.pyplot import title
from django.utils import timezone

# import user model 
from django.contrib.auth.models import User
# Create your models here
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author mein user foreign key se add aur delete krny k liya parameter mein on_delete add kiya
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

#dender method is that start with __
    def __str__(self):
        return self.title