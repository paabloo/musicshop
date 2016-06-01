from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()
    product_pk = forms.IntegerField()

    def clean_quantity(self):
        value = self.cleaned_data['quantity']
        if 0 < value < 100:
            return value
        # dodanie bledu
