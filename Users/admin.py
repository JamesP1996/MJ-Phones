from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import admin
from .models import  Profile


# Register your models here.
# Register a User Profile Model in the Admin.py 
# User Profile Contains Extra Like Addresses
class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Users'
    
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Profile)

