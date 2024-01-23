from django.db import models
from django.contrib.auth.models import User  # Importez User

class Client(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=255)  # Correction de la longueur maximale
    password = models.CharField(max_length=255)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()