from django.shortcuts import render

# Create your views here.
def cart_view(request):
    if request.user.is_authenticated:
        return render(request,'cart.html')
