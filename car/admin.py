
from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'model', 'price')
    list_filter = ('brand', 'model')
