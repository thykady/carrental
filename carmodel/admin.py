from django.contrib import admin
from .models import Model

@admin.register(Model)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand')

