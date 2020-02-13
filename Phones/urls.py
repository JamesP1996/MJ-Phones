from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='MJ-Phones-Home'),
    path('phones/',views.phones,name='MJ-Phones-Devices'),
    path('accessories/',views.accessories,name='MJ-Phones-Accessories'),
    path('compare/',views.comparePhones,name='MJ-Phones-Compare-Phones')
    
]
