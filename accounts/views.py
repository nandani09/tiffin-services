from django.shortcuts import render



from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import BuyerRegistrationForm, SellerRegistrationForm

def register_buyer(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register/buyer/')  # Replace 'home' with your desired redirect URL
    else:
        form = BuyerRegistrationForm()
    return render(request, 'accounts/register_buyer.html', {'form': form})

def register_seller(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register/seller/')  # Replace 'home' with your desired redirect URL
    else:
        form = SellerRegistrationForm()
    return render(request, 'accounts/register_seller.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')