from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100)  
    origin = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='brand_images/', default='default_image.jpg')

    def __str__(self):
        return self.name
