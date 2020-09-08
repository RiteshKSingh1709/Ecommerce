from django.shortcuts import render
from .models import Product,Rating
# Create your views here.

def product_display(request,product_id):
    print(product_id)
    p = Product.objects.get(pk=product_id)
    print(p.product_name,p.product_type,p.description)
    if request.user.is_authenticated:
        return render(request,'product.html')
