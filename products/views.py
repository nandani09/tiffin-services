from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'  # Use the same template for listing and creating

    def form_valid(self, form):
        form.instance.seller = self.request.user  # Set the seller to the current logged-in user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('products:product_list')  # Redirect to the product list after saving

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')
