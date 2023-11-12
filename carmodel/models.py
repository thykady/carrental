
from django.db import models

class Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('carmark.Brand', on_delete=models.CASCADE)  

    def __str__(self):
        return self.name
