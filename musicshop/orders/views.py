from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, FormView, TemplateView, CreateView
from django.contrib import messages
from musicshop.orders.forms import AddToCartForm, OrderForm
from musicshop.products.models import Product
from musicshop.orders.models import Order
from django.core.urlresolvers import reverse_lazy
from .models import OrderProduct


class AddToCartView(FormView):
    # template_name = 'add_to_cart.html'
    form_class = AddToCartForm

    def form_valid(self, form):
        pk = str(form.cleaned_data['product_pk'])
        quantity = form.cleaned_data['quantity']
        orders = self.request.session.get('orders', {})
        if pk not in orders:
            orders[pk] = 0
        orders[pk] += quantity
        self.request.session['orders'] = orders
        messages.success(self.request, "Dodano produkt")
        return super(AddToCartView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Seler jest ladny!')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.request.GET['next']


class RemoveFromCartView(RedirectView):
    pattern_name = 'orders:cart'

    def get(self, *args, **kwargs):
        pk = self.request.GET.get('pk')
        if pk and 'orders' in self.request.session:
            orders = self.request.session['orders']
            orders.pop(str(pk), None)
            self.request.session['orders'] = orders
            messages.success(self.request, 'Usunieto product')
        return super(RemoveFromCartView, self).get(*args, **kwargs)


class CartView(TemplateView):
    template_name = 'orders/cart.html'

    def get_context_data(self):
        orders = self.request.session.get('orders', {})
        ids = orders.keys()
        products_dict = Product.objects.in_bulk(ids)
        for pk, value in orders.items():
            product = products_dict[int(pk)]
            product.quantity = value
            product.price_all = product.price * product.quantity
        products = products_dict.values()
        results = {
            'products': products,
            'total': sum(obj.price_all for obj in products)
        }
        return results


class OrderPreperaView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_prepare.html'
    success_url = reverse_lazy('products:list')

    def form_valid(self, form):
        result = super(OrderPreperaView, self).form_valid(form)
        messages.success(self.request, 'Zlozono zamowienie')
        orders = self.request.session['orders']
        from musicshop.products.models import Product
        products = Product.objects.in_bulk(orders)

        for product_id, quantity in orders.items():
            product_id = int(product_id)
            op = OrderProduct()
            op.product_id = product_id
            op.quantity = quantity
            op.order = form.instance
            op.save()

            products[product_id].quantity -= quantity
            products[product_id].save()

        del self.request.session['orders']
        return result
