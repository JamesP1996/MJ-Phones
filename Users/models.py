from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField(max_length=300,blank=True)
    phoneNumber = models.CharField(max_length = 15, blank=True)
 
def __str__(self):
    return f'{self.user.username} Profile'

def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

