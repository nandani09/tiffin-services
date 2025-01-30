from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Buyer model
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

# Seller model

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50, blank=True, null=True)  # Add city
    pincode = models.CharField(max_length=10, blank=True, null=True)  # Add pincode
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.shop_name


# Product model linked to Seller
class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# models.py
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Seller)
def create_user_for_seller(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(
            username=instance.shop_name,  # Ensure this is unique
            password='default_password'  # Or generate a random password
        )






class Tiffin(models.Model):
    MEAL_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    meal = models.CharField(max_length=20, choices=MEAL_CHOICES)
    image = models.ImageField(upload_to='tiffins/')
    ingredients = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
