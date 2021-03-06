from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,ProfileRegisterForm

# Create your views here.

# Register View
def register(request):
    # If Request is == POST. Add the Two Forms Created in Forms.py. Validate them and clean the data and then save the information.
    # If the Information is Incorrect, Redirect to the Register Form which should now display Errors.
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.refresh_from_db() #load the profile instance created by signal
            username = form.cleaned_data.get('username')
            profile_form = ProfileRegisterForm(request.POST,instance = user.profile)
            profile_form.full_clean()
            profile_form.save()
            messages.success(request, f'Account Created for {username}!')
            return redirect('MJ-Phones-Login')
    else:
        form = UserRegisterForm()
        profile_form = ProfileRegisterForm()
    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request,'users/register.html', context)


