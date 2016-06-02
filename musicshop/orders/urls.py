"""musicshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from musicshop.orders.views import AddToCartView, CartView, RemoveFromCartView, order_prepare_view


urlpatterns = [
    url(r'^add-to-cart/$', AddToCartView.as_view(), name='add_to_cart'),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^remove-from-cart/$', RemoveFromCartView.as_view(), name='remove_from_cart'),
    url(r'^prepare/$', order_prepare_view, name='prepare'),
]
