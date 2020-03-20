from django.contrib import admin
from django.urls import path
from . import  views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='MJ-Phones-Home'),
    path('phones/',views.phones,name='MJ-Phones-Devices'),
    path('accessories/',views.accessories,name='MJ-Phones-Accessories'),
    path('compare/',views.comparePhones,name='MJ-Phones-Compare-Phones'),
    path('charge/<int:phone_id>/',views.charge,name="MJ-Phone-Charge")
]
