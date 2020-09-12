from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from User.models import Member
from Product.models import Product
from .models import Cart
# Create your views here.

@login_required
def cart_view(request):
    member = Member.objects.get(user=request.user.id)
    cartObj = Cart.objects.filter(member_id=member.id)
    context = {'data' : [],'total' : 0.0 }
    total = 0
    for c in cartObj:
        p = Product.objects.get(pk = c.product_id.id)
        context['data'].append(
            {
                'id'            : c.id,   
                'product_img'   : p.img_source,
                'product_name'  : p.product_name,
                'product_desc'  : p.description,
                'product_price' : p.price,
                'quantity'      : c.quantity,
                'subtotal'      : c.quantity * p.price
            }
        )
        total += c.quantity * p.price
    context['total'] = total
    return render(request,'cart.html',{'context' : context})

def delete_item(request,cart_id):
    if request.method == "GET":
        Cart.objects.get(pk = cart_id).delete()
        return cart_view(request)
