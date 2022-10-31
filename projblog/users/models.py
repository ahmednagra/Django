from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
# 1 to 1 relationship profile with user
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#dender     
    def __str__(self):
        return f'{self.user.username} Profile' 

    # resizing images for profile update
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.image.path)    