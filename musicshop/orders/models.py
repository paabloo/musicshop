from django.db import models
from musicshop.products.models import Product

class Order(models.Model):
    STATUS_NEW = 0
    STATUS_CANCELED = 1
    STATUS_FINISHED = 2
    STAUTS_TYPES_CHOICES = [
        (STATUS_NEW, 'Nowe'),
        (STATUS_CANCELED, 'Anulowane'),
        (STATUS_FINISHED, 'Zrealizowane'),
    ]
    client_name = models.CharField(max_length=255, verbose_name='Nazwa Klienta')
    address = models.CharField(max_length=1023, verbose_name="Adres")
    status = models.IntegerField(choices=STAUTS_TYPES_CHOICES, default=STATUS_NEW)

    class Meta:
        verbose_name = 'Zamowienie'
        verbose_name_plural = 'Zamowienia'

    def __str__ (self):
        return '{} - {}'.format(self.client_name, self.status)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name="order_products")
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Zamowiony produkt'
        verbose_name_plural = 'Zamowione produkty'

    def __str__ (self):
        return '{} - {}'.format(self.product, self.quantity)
