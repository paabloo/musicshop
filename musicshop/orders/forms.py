from django import forms
from musicshop.orders.models import Order, OrderProduct


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()
    product_pk = forms.IntegerField()

    def clean_quantity(self):
        value = self.cleaned_data['quantity']
        if value > 0:
            return value
        else:
            self.add_error('quantity', 'dupa')


class OrderForm(forms.ModelForm):

    client_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )


    class Meta:
        model = Order
        fields = ['client_name', 'address']


class OrderProducForm(forms.ModelForm):

    quantity = forms.IntegerField(
        # widget=
    )
