from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView
app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product_form/', ProductCreateView.as_view(), name='product_form'),
    path('<int:pk>/product_form/', ProductUpdateView.as_view(), name='product_update'),
    
]
