from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_seller')
    shop_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.shop_name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Updated

    def __str__(self):
        return self.name
