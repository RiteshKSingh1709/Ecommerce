from django.db import models

# Create your models here.


class Member(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    fullname = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.username
