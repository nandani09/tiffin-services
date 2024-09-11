# accounts/urls.py

from django.urls import path
from . import views
from .views import register_buyer, register_seller,home

urlpatterns = [
    path('register/buyer/', register_buyer, name='register_buyer'),
    path('register/seller/', register_seller, name='register_seller'),
    path('', home , name='home'),
    
]
