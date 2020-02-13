from django.shortcuts import render
from django.http import HttpResponse

phones = [
    {
        'brand': 'Samsung',
        'name': 'Galaxy S10',
        'screen': '1920x1080'
    }
]


# Create your views here.
def home(request):
    context = {
        'phones': phones
    }
    return render(request, 'phone/home.html', context)

def phones(request):
    return render(request, 'phone/phones.html', {'title': 'Devices'})

def accessories(request):
    return render(request,'phone/accessories.html', {'title':'Accessories'})

def comparePhones(request):
    return render(request,'phone/compare.html',{'title':'Compare-Phones'})
