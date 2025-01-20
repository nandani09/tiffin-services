from django.contrib import admin
# admin.py
from django.contrib import admin
from .models import Buyer, Seller, Product

# Buyer Admin
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number')  # Fields to display in the admin list view
    search_fields = ('user__username', 'phone_number')  # Search functionality for user and phone number
    list_filter = ('address',)  # Add filtering by address (optional)

# Seller Admin
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'shop_name', 'address', 'phone_number')  # Fields to display in the admin list view
    search_fields = ('user__username', 'shop_name', 'phone_number')  # Search by username, shop name, or phone number
    list_filter = ('shop_name',)  # Filter by shop name (optional)

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'price', 'available')  # Fields to display in the admin list view
    list_filter = ('available', 'seller')  # Filter by availability and seller
    search_fields = ('name', 'seller__shop_name')  # Search by product name or seller's shop name
    list_editable = ('price', 'available')  # Allow price and availability to be edited directly in the list view
    ordering = ('-price',)  # Order products by price in descending order


