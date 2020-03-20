from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AddPhone
from .models import AddAccessory
from Users.models import Profile
import stripe;

stripe.api_key = "sk_test_oyEMcOGEo2MMg26uQmdbkWp200S5ZbzZ5U"

# Create your views here.

def home(request):
    return render(request, 'phone/home.html')


def phones(request):
    context = {
        'phones': AddPhone.objects.all(),
        'key' : "pk_test_coYGFy8Mcb6eZA35eCz3aCWK00UK5mxZ4t"
        
    }
    return render(request, 'phone/phones.html', context)


def accessories(request):
    context= {
        'accessories': AddAccessory.objects.all()
    }
    return render(request, 'phone/accessories.html', context)


def comparePhones(request):
    return render(request, 'phone/compare.html', {'title': 'Compare-Phones'})

def charge(request,phone_id): # new
   
    phone = AddPhone.objects.get(pk=phone_id)
    current_user = request.user
    user = Profile.objects.get(user_id=current_user.id)
    price = str(round(phone.stripe_price()))
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount= price,
            currency='eur',
            description=phone.brand + phone.name + " Being Sent to " + user.address,
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html',{"address":user.address})
