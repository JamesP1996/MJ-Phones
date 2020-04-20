from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import string, random, datetime

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


# Random String Method
def random_string():
    return ''.join(random.choice(string.ascii_letters) for m in range(6))


# Create a Order when user buys a product.
class Order(models.Model):
    username = models.CharField(max_length=40)

    phoneProductID = models.IntegerField(blank=True, null=True)
    phoneName = models.CharField(max_length=40, blank=True, null=True)

    accessoryProductID = models.IntegerField(blank=True, null=True)
    accessoryName = models.CharField(max_length=40, blank=True, null=True)
    # Generate Random Ref. Number
    referrence = models.CharField(
        max_length=6,
        blank=True,
        editable=False,
        unique=True,
        default=random_string
    )
    date_ordered = models.DateTimeField(
        editable=False,
        default=datetime.datetime.today()
    )

    # For Admin View
    def __str__(self):
        return 'Reference: %s ' % self.referrence

class compare(models.Model):


    def __str__(self):
        return self.name