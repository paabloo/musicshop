from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()
    product_pk = forms.IntegerField()

    def clean_quantity(self):
        value = self.cleaned_data['quantity']
        if value > 0:
            return value
        else:
            self.add_error('quantity', 'dupa')
