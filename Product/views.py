from django.shortcuts import render
from .models import Product,Rating

# Create your views here.

def product_display(request,product_id):
    p = Product.objects.get(pk=product_id)
    print(p.product_name,p.product_type,p.description)
    return render(request,'product.html',{'product' : p})

