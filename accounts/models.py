from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_buyer=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)

class buyer(models.Model):
    name=models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
