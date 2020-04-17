from django.contrib import admin
from .models import AddPhone
from .models import AddAccessory

#Register AddPhone and AddAccessory on the Admin.py Page
admin.site.register(AddPhone)
admin.site.register(AddAccessory)
