from django.db import models

class ImageUpload(models.Model):
    name = models.CharField(max_length=50)
    add_image = models.ImageField(upload_to='images/')
