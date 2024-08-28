from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, buyer, Seller

class BuyerRegistrationForm(UserCreationForm):
    address = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_buyer = True
        if commit:
            user.save()
            buyer.objects.create(user=user, address=self.cleaned_data['address'])
        return user

class SellerRegistrationForm(UserCreationForm):
    business_name = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'business_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True
        if commit:
            user.save()
            Seller.objects.create(user=user, business_name=self.cleaned_data['business_name'])
        return user
