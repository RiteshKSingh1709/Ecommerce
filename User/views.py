from django.shortcuts import render,redirect
from .models import Member
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from Product.models import Product
from Cart.views import cart_view

# import libraries
import random
# Create your views here.


def home(request):
    products = Product.objects.all()
    for product in products:
        product.old_price = product.price + random.randint(1,10)
    return render(request,'home.html',{'products' : products})

def login(request):
    pass

def signup(request):
    if request.method == "POST":
        u = User.objects.create_user(
            request.POST['username'],
            request.POST['email'],
            request.POST['password'],
            is_active = 1
        )
        m = Member(
            user=u,
            username=request.POST["username"],
            password=request.POST["password"],
            email=request.POST["email"],
            fullname=request.POST["fullname"],
            address=request.POST["address"],
            phone=request.POST['phone']
        )
        u.save()
        m.save()
        return redirect(home)
    return render(request,'signup.html')

def profile(request):
    member = Member.objects.get(user=request.user.id)
    user = User.objects.get(username = member.user)
    print(member)
    if request.method == "POST": 
        print(request.POST['username'])
        user.username = request.POST['username']
        user.set_password(request.POST['password'])
        update_session_auth_hash(request, request.user)
        user.save()
        member.username = request.POST['username']
        member.password = request.POST['password']
        member.email = request.POST['email']
        member.save()
        return render(request,'profile.html',{'context' : "Profile Update successfully .. "})
    return render(request,'profile.html',{'member' : member})