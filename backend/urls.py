from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define the homepage URL
    path('buyer_register/', views.buyer_register, name='buyer_register'),
    path('seller_register/', views.seller_register, name='seller_register'),
    path('products/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('thank-you/', views.thank_you, name='thank_you'), 
    path('login/', views.seller_login, name='seller_login'),
    path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
]
