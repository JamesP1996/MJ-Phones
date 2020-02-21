from django.shortcuts import render
from django.http import HttpResponse
from .models import AddPhone
from .models import AddAccessory
# Create your views here.
def home(request):
    return render(request, 'phone/home.html')


def phones(request):
    context = {
        'phones': AddPhone.objects.all()
    }
    return render(request, 'phone/phones.html', context)


def accessories(request):
    context= {
        'accessories': AddAccessory.objects.all()
    }
    return render(request, 'phone/accessories.html', context)


def comparePhones(request):
    return render(request, 'phone/compare.html', {'title': 'Compare-Phones'})
