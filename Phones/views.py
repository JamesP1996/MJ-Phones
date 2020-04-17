from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AddPhone
from .models import AddAccessory
from Users.models import Profile
import stripe;

#Stripe API Key for My Stripe DashBoard Account <Used for Charging/E-Commerce Purchasing>
stripe.api_key = "sk_test_oyEMcOGEo2MMg26uQmdbkWp200S5ZbzZ5U"

# Setup a Re-Useable Query Validator
def is_valid_queryparam(param):
    return param != '' and param is not None

# Create Home View which will Render Home.html File
def home(request):
    return render(request, 'phone/home.html')

# Create a Phone View Which Will Take in Queries and Return the Phones from the Database
def phones(request):
    # Our Query Set
    querySet = AddPhone.objects.all()
    # Different Queries we can look for eg. name,brand,price,etc..
    name_contains_query = request.GET.get('name_contains')
    brand_contains_query = request.GET.get('brand_contains')
    min_price_query = request.GET.get('min_price')
    max_price_query = request.GET.get('max_price')
    min_space_query = request.GET.get('min_space')
    min_ram_query = request.GET.get('min_ram')
    min_cpuspeed_query = request.GET.get('min_cpuspeed')
    min_cpucores_query = request.GET.get('min_cpucores')
    min_display_query = request.GET.get('min_display')
    min_width_query = request.GET.get('min_width')
    min_height_query = request.GET.get('min_height')
    min_mcamera_query = request.GET.get('min_mcamera')
    min_fcamera_query = request.GET.get('min_fcamera')
    min_battery_query = request.GET.get('min_battery')
    
    # If the inputted name is a valid query. Filter the Query Set where the name of the phone = "name_contains_query"
    if is_valid_queryparam(name_contains_query):
        querySet = querySet.filter(name__icontains = name_contains_query)
        
    # If the inputted brand is a valid query. Filter the Query Set where the brand of the phone = "brand_contains_query"
    if is_valid_queryparam(brand_contains_query):
        querySet = querySet.filter(brand__icontains = brand_contains_query)
        
    #  Filter the Query Set by Minimum/Equal to Phone Price.
    if is_valid_queryparam(min_price_query):
        querySet = querySet.filter(price__gte=min_price_query)
    
    #  Filter the Query Set by Maximum/Equal to Phone Price.
    if is_valid_queryparam(max_price_query):
        querySet = querySet.filter(price__lte=max_price_query)
        
    #  Filter the Query Set by Minimum/Equal Display to Phone Memory Space.   
    if is_valid_queryparam(min_space_query):
        querySet = querySet.filter(internalMemory__gte=min_space_query)  
        
    #  Filter the Query Set by Minimum/Equal to Ram(gb).  
    if is_valid_queryparam(min_ram_query):
        querySet = querySet.filter(ram__gte=min_ram_query) 
        
    #  Filter the Query Set by Minimum/Equal to CPU Speed. 
    if is_valid_queryparam(min_cpuspeed_query):
        querySet = querySet.filter(cpu__gte=min_cpuspeed_query) 
    
    #  Filter the Query Set by Minimum/Equal to CPU Cores.   
    if is_valid_queryparam(min_cpucores_query):
        querySet = querySet.filter(cpu_cores__gte=min_cpucores_query) 
        
    #  Filter the Query Set by Minimum/Equal Display In Inches (Rounded).   
    if is_valid_queryparam(min_display_query):
        querySet = querySet.filter(display__gte=min_display_query) 
    
    #  Filter the Query Set by Minimum/Equal to Resolution Width.      
    if is_valid_queryparam(min_width_query):
        querySet = querySet.filter(width__gte=min_width_query)
        
    #  Filter the Query Set by Minimum/Equal to Resolution Width.      
    if is_valid_queryparam(min_height_query):
        querySet = querySet.filter(height__gte=min_height_query)
        
    #  Filter the Query Set by Minimum/Equal to Main Camera Megapixel.      
    if is_valid_queryparam(min_mcamera_query):
        querySet = querySet.filter(mainCamera__gte=min_mcamera_query)
        
    #  Filter the Query Set by Minimum/Equal to Front Camera Megapixel.      
    if is_valid_queryparam(min_fcamera_query):
        querySet = querySet.filter(frontCamera__gte=min_fcamera_query)
        
    # Filter the Query Set by Minimum/Equal to Battery Capacity
    if is_valid_queryparam(min_battery_query):
        querySet = querySet.filter(battery__gte=min_battery_query)    
        
    #Context of the Phone View , we will pass in the Query Set and The Stripe Public Key
    context = {
        'phones': querySet,
        'key' : "pk_test_coYGFy8Mcb6eZA35eCz3aCWK00UK5mxZ4t"
        
    }
    return render(request, 'phone/phones.html', context)

# Create a Accessory View Which Will Take in Queries and Return the Accessories from the Database
def accessories(request):
    
    querySet = AddAccessory.objects.all()
    category = AddAccessory.objects.values('category').distinct()
    
    name_contains_query = request.GET.get('name_contains')
    category_contains_query = request.GET.get('category_contains')
    min_price_query = request.GET.get('min_price')
    max_price_query = request.GET.get('max_price')
    
    
     # If the inputted name is a valid query. Filter the Query Set where the name of the phone = "name_contains_query"
    if is_valid_queryparam(name_contains_query):
        querySet = querySet.filter(name__icontains = name_contains_query)
        
    # If the inputted name is a valid query. Filter the Query Set where the name of the phone = "name_contains_query"
    if is_valid_queryparam(category_contains_query) and category_contains_query != 'Select...':
        querySet = querySet.filter(category__icontains = category_contains_query)
        
     #  Filter the Query Set by Minimum/Equal to Phone Price.
    if is_valid_queryparam(min_price_query):
        querySet = querySet.filter(price__gte=min_price_query)
    
    #  Filter the Query Set by Maximum/Equal to Phone Price.
    if is_valid_queryparam(max_price_query):
        querySet = querySet.filter(price__lte=max_price_query)
    
    context= {
        'accessories': querySet,
        'categories' : category,
        'key' : "pk_test_coYGFy8Mcb6eZA35eCz3aCWK00UK5mxZ4t"

    }
    return render(request, 'phone/accessories.html', context)

# Compare Phones View Where the User can Compare one phone to another
def comparePhones(request):
    return render(request, 'phone/compare.html', {'title': 'Compare-Phones'})

# Charge View Where the Phone a User has bought along with their shipping address will be displayed on Purchase of a Mobile Device
def charge(request,phone_id):
    phone = AddPhone.objects.get(pk=phone_id)
    current_user = request.user
    user = Profile.objects.get(user_id=current_user.id)
    price = str(round(phone.stripe_price()))
    # If the Request is a POST request create a stripe charge with the price,currency and description of Phone+Shipping Details
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount= price,
            currency='eur',
            description=phone.brand + phone.name + " Being Sent to " + user.address,
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html',{"address":user.address})
    
# Charge View Where the Accesory a User has bought along with their shipping address will be displayed on Purchase of an Accessory
def charge2(request,accessory_id):
    accessory = AddAccessory.objects.get(pk=accessory_id)
    current_user = request.user
    user = Profile.objects.get(user_id=current_user.id)
    price = str(round(accessory.stripe_price()))
    # If the Request is a POST request create a stripe charge with the price,currency and description of Accessory+Shipping Details
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount= price,
            currency='eur',
            description=accessory.name + "CATEGORY:" + accessory.category + " Being Sent to " + user.address,
            source=request.POST['stripeToken']
        )
        return render(request, 'charge2.html',{"address":user.address})
