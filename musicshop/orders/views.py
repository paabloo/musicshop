from django.views.generic import RedirectView, FormView
from django.contrib import messages
from musicshop.orders.forms import AddToCartForm

class AddToCartView_old(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return self.request.GET['next']

class AddToCartView(FormView):
    # template_name = 'contact.html'
    form_class = AddToCartForm

    def form_valid(self, form):
        messages.success(self.request, 'Seler jest brzydki!')
        return super(AddToCartView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Seler jest ładny!')
        return super(AddToCartView, self).form_invalid(form)

    def get_success_url(self):
        return self.request.GET['next']
