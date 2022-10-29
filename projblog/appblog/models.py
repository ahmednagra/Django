from django.db import models
from django.utils import timezone
from django.urls import reverse

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

# is se  new post create k bad browser redirect to detail page
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    