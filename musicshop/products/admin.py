from django.contrib import admin
from musicshop.products.models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    list_editable = ('quantity',)
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)


