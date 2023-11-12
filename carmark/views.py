from django.shortcuts import render, redirect, get_object_or_404
from carmark.models import Brand
from carmark.forms import BrandForm  



def home(request):
    return render(request, 'carmark/index.html')




def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'carmark/index.html', {'brands': brands})


def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    return render(request, 'carmark/show.html', {'brand': brand})


def brand_create(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
    else:
        form = BrandForm()

    return render(request, 'carmark/create.html', {'form': form})


def brand_update(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)

    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
    else:
        form = BrandForm(instance=brand)

    return render(request, 'carmark/update.html', {'form': form, 'brand': brand})


def brand_delete(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)

    if request.method == 'POST':
        brand.delete()
        return redirect('brand_list')

    return render(request, 'carmark/delete.html', {'brand': brand})

