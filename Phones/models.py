from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Phone Data Model for SQL LITE
class AddPhone(models.Model):
    brand = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    image = models.TextField()
    price = models.FloatField()
    colour = models.CharField(max_length=20)
    height = models.IntegerField()
    width = models.IntegerField()
    os = models.CharField(max_length=20)
    display = models.FloatField()
    mainCamera = models.FloatField()
    frontCamera = models.FloatField()
    processor = models.CharField(max_length=30)
    cpu = models.FloatField()
    cpu_cores = models.IntegerField()
    ram = models.IntegerField()
    internalMemory = models.IntegerField()
    fourG = models.BooleanField()
    video = models.CharField(max_length=20)
    battery = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def stripe_price(self):
        return self.price * 100

# Accessory Data Model For SQL LITE
class AddAccessory(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField()
    image = models.TextField()
    
    def stripe_price(self):
        return self.price * 100

    def __str__(self):
        return self.name
