from django.views.generic import ListView, DetailView
from musicshop.products.models import Product

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
