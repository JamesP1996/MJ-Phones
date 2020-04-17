from django.contrib import admin
from django.urls import path
from . import  views
from django.contrib.auth import views as auth_views

# Each URL Pattern that the Site can Re-Direct to Within the Phones Folder
urlpatterns = [
    path('', views.home, name='MJ-Phones-Home'),
    path('phones/',views.phones,name='MJ-Phones-Devices'),
    path('accessories/',views.accessories,name='MJ-Phones-Accessories'),
    path('compare/',views.comparePhones,name='MJ-Phones-Compare-Phones'),
    path('charge/<int:phone_id>/',views.charge,name="MJ-Phone-Charge"),
    path('charge2/<int:accessory_id>',views.charge2,name="MJ-Phones-Charge2")
]
