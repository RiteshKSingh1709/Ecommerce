from django.shortcuts import render
from .models import Member
from Product.models import Product
# Create your views here.


def home(request):
    if request.method=="POST":
        pass
    p = Product.objects.all()
    print(p)
    return render(request,'home.html',{'products' : p})

def login(request):
    if request.method == "POST":
        request_data = request.POST
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        m = Member(
            username=request.POST["username"],
            password=request.POST["password"],
            email=request.POST["email"],
            fullname=request.POST["fullname"],
            address=request.POST["address"],
            phone=8276079012
        )
        m.save()
        return render(request,'home.html')
    return render(request,'signup.html')