from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create a User Registration Form that Takes in username,email,password,password2,first name and last name
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name',
                  'last_name']
        
# Create the Extended User Form known as UserProfile Model and take in an address and phone number.  
class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','phoneNumber']