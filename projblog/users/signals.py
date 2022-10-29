# this model is used to give automatically profiles for every user
from django.db.models.signals import post_save
# Here User model is called Sender
from django.contrib.auth.models import User
# define receiver that got signal and perform some task
from django.dispatch import receiver

# import profile from model and send and creating a prosile in function
from .models import profile


#decorator function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


#decorator and save profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        profile.objects.save()
                