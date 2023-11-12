
from django.shortcuts import render, redirect, get_object_or_404
from .models import Model
from .forms import CarModelForm 


def carmodel_list(request):
    carmodels = Model.objects.all()
    return render(request, 'carmodel/index.html', {'carmodels': carmodels})


def carmodel_detail(request, carmodel_id):
    carmodel = get_object_or_404(Model, pk=carmodel_id)
    return render(request, 'carmodel/show.html', {'carmodel': carmodel})


def carmodel_create(request):
    if request.method == 'POST':
        form = CarModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carmodel_list')
    else:
        form = CarModelForm()

    return render(request, 'carmodel/create.html', {'form': form})


def carmodel_update(request, carmodel_id):
    carmodel = get_object_or_404(Model, pk=carmodel_id)

    if request.method == 'POST':
        form = CarModelForm(request.POST, instance=carmodel)
        if form.is_valid():
            form.save()
            return redirect('carmodel_list')
    else:
        form = CarModelForm(instance=carmodel)

    return render(request, 'carmodel/update.html', {'form': form, 'carmodel': carmodel})


def carmodel_delete(request, carmodel_id):
    carmodel = get_object_or_404(Model, pk=carmodel_id)

    if request.method == 'POST':
        carmodel.delete()
        return redirect('carmodel_list')

    return render(request, 'carmodel/delete.html', {'carmodel': carmodel})
