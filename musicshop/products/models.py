from django.db import models
from django.core.urlresolvers import reverse

class ProductCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nazwa')

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = 'Kategoria towarow'
        verbose_name_plural = 'Kategorie towarow'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nazwa')
    category = models.ForeignKey(ProductCategory, blank=True, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Towar'
        verbose_name_plural = 'Towary'

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'pk': self.pk})
