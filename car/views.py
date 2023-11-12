
from django.shortcuts import render, redirect, get_object_or_404
from car.models import Car
from car.forms import CarForm  
from carmodel.models import Model
from carmark.models import Brand


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car/show.html', {'car': car})


def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()

    return render(request, 'car/create.html', {'form': form})


def car_update(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)

    return render(request, 'car/update.html', {'form': form, 'car': car})


def car_delete(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    if request.method == 'POST':
        car.delete()
        return redirect('car_list')

    return render(request, 'car/delete.html', {'car': car})
