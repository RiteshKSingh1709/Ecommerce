from django.shortcuts import render
from .models import Member
# Create your views here.


def home(request):
    return render(request,'home.html')

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