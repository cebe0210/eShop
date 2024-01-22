from django.db import models

class Client(models.Model):
    username = models.CharField(max_lenght=100)
    email = models.CharField(unique=True)
    password = models.CharField(max_lenght=255)
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    quantity = models.CharField(max_length=16)
    price = models.CharField(max_length=16)
    