from django import forms
from .models import Model

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name', 'brand']  
