from django.contrib import admin
from .models import Product,Rating,Comment
from User.models import Member

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','description']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['value','product_id','member_id']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment','product_id','member_id']