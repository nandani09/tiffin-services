from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Buyer, Seller, Product
from django.contrib.auth.decorators import login_required

# Buyer registration view
def buyer_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Buyer.objects.create(user=user, address=request.POST['address'], phone_number=request.POST['phone_number'])
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'backend/buyer_register.html', {'form': form})

# Seller registration view
def seller_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Seller.objects.create(user=user, shop_name=request.POST['shop_name'], address=request.POST['address'], phone_number=request.POST['phone_number'])
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'backend/seller_register.html', {'form': form})

# Product list view for buyers
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'backend/product_list.html', {'products': products})

# Add product view for sellers
@login_required
def add_product(request):
    seller = Seller.objects.get(user=request.user)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Product.objects.create(seller=seller, name=name, description=description, price=price)
        return redirect('product_list')
    return render(request, 'backend/product_form.html')
def home(request):
    return render(request, 'backend/home.html')


