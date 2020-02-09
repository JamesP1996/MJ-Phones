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

def about(request):
    return render(request, 'phone/about.html', {'title': 'About'})
