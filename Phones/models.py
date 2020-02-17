from django.db import models

class AddPhone(models.Model):
    brand = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    image = models.TextField()
    price = models.FloatField()
    colour = models.CharField(max_length=20)
    height = models.FloatField()
    width = models.FloatField()
    os = models.CharField(max_length=20)
    display = models.FloatField()
    mainCamera = models.FloatField()
    frontCamera = models.FloatField()
    processor = models.CharField(max_length=20)
    cpu = models.FloatField()
    ram = models.IntegerField()
    internalMemory = models.IntegerField()
    fourG = models.BooleanField()
    video = models.CharField(max_length=20)
    battery = models.IntegerField()
    descrption = models.TextField()

    def __str__(self):
        return self.name

class AddAccessory(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    mail = models.EmailField()
    address = models.TextField()
    phoneNumber = models.IntegerField()
    postCode = models.CharField(max_length=20)

    def __str__(self):
        return self.name
