from django.db import models
from Product.models import Product
from User.models import Member
# Create your models here.
class Cart(models.Model):
    product_id = models.ForeignKey(Product,null=True, blank=True, on_delete=models.SET_NULL)
    member_id = models.ForeignKey(Member,null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()

