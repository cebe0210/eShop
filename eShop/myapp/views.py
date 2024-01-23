# from django.shortcuts import render
# from .models import Item

# def shop_view(request):
    
#     cart_items = Item.objects.all()

#     context = {
#         'cart_items': cart_items,
#     }

#     return render(request, 'frontend/shop.html', context)

from django.shortcuts import render
from .models import Item

def test_view(request):
    items = Item.objects.all()
    return render(request, 'myapp/test.html', {'items': items})
