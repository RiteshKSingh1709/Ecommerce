from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    fullname = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.username

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     print("sdfsd",created,instance,sender)
#     if created:
#         Member.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     print("popowpo",instance,sender)
#     instance.member.save()
