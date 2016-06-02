from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, FormView, TemplateView
from django.contrib import messages
from musicshop.orders.forms import AddToCartForm
from musicshop.products.models import Product

class AddToCartView_old(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return self.request.GET['next']

class AddToCartView(FormView):
    # template_name = 'add_to_cart.html'
    form_class = AddToCartForm

    def form_valid(self, form):
        pk = str(form.cleaned_data['product_pk'])
        quantity = form.cleaned_data['quantity']
        orders = self.request.session.get('orders', {})
        print(type(pk))
        if pk not in orders:
            orders[pk] = 0
        orders[pk] += quantity
        self.request.session['orders'] = orders
        messages.success(self.request, str(orders))
        return super(AddToCartView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Seler jest ładny!')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.request.GET['next']


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
