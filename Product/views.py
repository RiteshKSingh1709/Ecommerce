from django.shortcuts import render

# Create your views here.

def product_display(request):
    if request.user.is_authenticated:
        return render(request,'product.html')
