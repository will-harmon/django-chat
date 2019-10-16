from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
   pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    # location of the uploaded image will be in MEDIA_ROOT/images
    avatar = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username
