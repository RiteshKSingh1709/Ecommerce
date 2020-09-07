from django.db import models
from User.models import Member
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=50)
    description = models.TextField()
    stock = models.IntegerField()
    price = models.IntegerField()
    img_source = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.product_name
    
class Rating(models.Model):
    value = models.IntegerField()
    product_id = models.ForeignKey(Product,null=True, blank=True, on_delete=models.SET_NULL)
    member_id = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.value

class Comment(models.Model):
    member_id = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL)
    product_id = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    comment = models.TextField()
    
    def __str__(self):
        return self.comment