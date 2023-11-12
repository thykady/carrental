
from django.contrib import admin
from django.urls import path
from carmark.views import home, brand_create, brand_delete, brand_detail, brand_list, brand_update
from carmodel.views import carmodel_create, carmodel_delete, carmodel_detail, carmodel_list, carmodel_update
from car.views import car_create, car_delete, car_detail, car_list, car_update
from core.views import core_home
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_home, name='home'),
    path('core_home', core_home, name='core_home'),
    path('brand_create', brand_create, name='brand_create'),
    path('brand_list', brand_list, name='brand_list'),
    path('brand_delete/<int:brand_id>/', brand_delete, name='brand_delete'),
    path('brand_update/<int:brand_id>', brand_update, name='brand_update'),
    path('brand_detail<int:brand_id>/', brand_detail, name='brand_detail'),

    path('carmodel_create', carmodel_create, name='carmodel_create'),
    path('carmodel_delete/<int:carmodel_id>/', carmodel_delete, name='carmodel_delete'),
    path('carmodel_detail/<int:carmodel_id>/', carmodel_detail, name='carmodel_detail'),
    path('carmodel_list', carmodel_list, name='carmodel_list'),
    path('carmodel_update/<int:carmodel_id>/', carmodel_update, name='carmodel_update'),

    path('car_create', car_create, name='car_create'),
    path('car_delete/<int:car_id>/', car_delete, name='care_delete'),
    path('car_detail/<int:car_id>/', car_detail, name='car_detail'),
    path('car_list', car_list, name='car_list'),
    path('car_update/<int:car_id>/', car_update, name='car_update'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
