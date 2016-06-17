from django.conf.urls import url
from musicshop.orders.views import AddToCartView, CartView, RemoveFromCartView, OrderPreperaView


urlpatterns = [
    url(r'^add-to-cart/$', AddToCartView.as_view(), name='add_to_cart'),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^remove-from-cart/$', RemoveFromCartView.as_view(), name='remove_from_cart'),
    url(r'^prepare/$', OrderPreperaView.as_view(), name='prepare'),
]
