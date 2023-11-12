from django.shortcuts import render
from car.models import Car 

def core_home(request):
   
    vehicles = Car.objects.all()[:5]  
    
    context = {'vehicles': vehicles}
    return render(request, 'core/home.html', context)

