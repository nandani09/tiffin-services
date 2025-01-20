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
# views.py
from django.shortcuts import render, redirect
from .forms import SellerRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from django.contrib import messages


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SellerRegistrationForm
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def seller_register(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            # Get form data
            shop_name = form.cleaned_data['shop_name']
            password = form.cleaned_data['password']
            
            # Generate a unique username
            base_username = shop_name.lower().replace(" ", "_")
            username = base_username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}_{counter}"
                counter += 1
            
            try:
                # Create a new User
                user = User.objects.create_user(username=username, password=password)
                
                # Create the Seller object
                seller = form.save(commit=False)
                seller.user = user
                seller.save()

                # Redirect to the Thank You page
                return redirect('thank_you')
            except IntegrityError:
                # If something unexpected occurs
                form.add_error(None, "An unexpected error occurred. Please try again.")
        else:
            form.add_error(None, "Invalid data submitted. Please check and try again.")
    else:
        form = SellerRegistrationForm()

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
    return render(request, 'backend/dashboard.html')


def seller_login(request):
    return render(request, 'backend/seller_login.html')  # Replace 'login.html' with your template name

# views.py


def thank_you(request):
    return render(request, 'backend/thank_you.html') 
