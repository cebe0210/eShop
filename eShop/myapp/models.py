from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    # firstName = models.CharField(max_length=100)
    # lastName = models.CharField(max_length=100)
    # email = models.CharField(unique=True, max_length=255)
    # password = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
     
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=512)
    category = models.CharField(max_length=100)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255)
    on_sale = models.BooleanField(default=False) 

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()