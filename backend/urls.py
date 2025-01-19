from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define the homepage URL
    path('buyer_register/', views.buyer_register, name='buyer_register'),
    path('seller_register/', views.seller_register, name='seller_register'),
    path('products/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
]
