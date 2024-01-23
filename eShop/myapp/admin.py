from django.contrib import admin
from .models import Client, Item, Cart

admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Cart)

# Register your models here.
