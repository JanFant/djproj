from timeit import default_timer
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.

def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 1555),
        ('Desktop', 2555),
        ('Smartphone', 999),
    ]
    my_context = {
        "time_running": default_timer(),
        "products": products
    }
    return render(request, 'shopapp/shop-index.html', context=my_context)
