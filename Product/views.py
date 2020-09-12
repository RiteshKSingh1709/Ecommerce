from django.shortcuts import render,redirect
from .models import Product,Rating
from User.models import Member
from Cart.models import Cart

# Create your views here.

def product_display(request,product_id):
    product = Product.objects.get(pk=product_id)
    return render(request,'product.html',{'product' : product})

def add_to_cart(request,product_id):
    try:
        member = Member.objects.get(user=request.user.id)
    except Exception as e:
        return redirect('login')
    try:
        c = Cart.objects.get(member_id=member.id,product_id=product_id)
        c.quantity += 1
        c.save()
    except Cart.DoesNotExist:
        c = Cart(
            member_id = Member.objects.get(pk = member.id),
            product_id = Product.objects.get(pk = product_id),
            quantity = 1
        )
        c.save()
    product = Product.objects.get(pk=product_id)
    return render(request,'product.html',{'product' : product,'successMsg' : 'Item added to cart successfully ..'})

