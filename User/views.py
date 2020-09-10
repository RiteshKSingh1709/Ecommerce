from django.shortcuts import render,redirect
from .models import Member
from django.contrib.auth.models import User
from Product.models import Product
from Cart.views import cart_view
# Create your views here.


def home(request):
    p = Product.objects.all()
    return render(request,'home.html',{'products' : p})

def login(request):
    if request.method == "POST":
        m = Member.objects.get(username=request.POST['username'],password=request.POST['password'])
        if m is not None:
            return redirect(home)
        else:
            return render(request,'login.html',{'errorMsg' : "Login or Password is incorrect"})

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
            phone=8276079012
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
        user.password = request.POST['password']
        user.save()
        member.username = request.POST['username']
        member.password = request.POST['password']
        member.email = request.POST['email']
        member.save()
        return render(request,'profile.html',{'context' : "Profile Update successfully .. "})
    return render(request,'profile.html',{'member' : member})