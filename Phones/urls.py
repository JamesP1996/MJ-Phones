from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='MJ-Phones-Home'),
    path('about/',views.about,name='MJ-Phones-About')
]
