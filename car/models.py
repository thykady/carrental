
from django.db import models
from carmodel.models import Model  


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('carmark.Brand', on_delete=models.CASCADE)  
    model = models.ForeignKey(Model, on_delete=models.CASCADE)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/', default='default_image.jpg')


    def __str__(self):
        return self.name
    