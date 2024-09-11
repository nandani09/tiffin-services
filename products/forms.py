from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Price',
            'available': 'Available'
        }
        help_texts = {
            'name': 'Enter the name of the product.',
            'description': 'Provide a detailed description of the product.',
            'price': 'Enter the price of the product.',
            'available': 'Check if the product is available for purchase.',
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
