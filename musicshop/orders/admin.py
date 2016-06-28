# -*- coding: utf-8 -*-
import csv
from django.contrib import admin
from musicshop.orders.models import Order, OrderProduct
from django.http import HttpResponse


class OrderProductAdminInline(admin.TabularInline):
    model = OrderProduct
    fk_name = 'order'


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderProductAdminInline, )
    list_display = ('client_name', 'address', 'status', 'get_total_price')
    fields = ('client_name', 'address', 'status', 'get_total_price')
    readonly_fields = ('get_total_price', )
    actions = ('generate_report', )

    def get_total_price(self, obj):
        return "{0:.2f}".format(sum(map(lambda p: p.product.price * p.quantity, obj.order_products.all())))
    get_total_price.short_description = 'total'

    def generate_report(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename=report.csv'
        writer = csv.writer(response)

        writer.writerow(('ID zamówienia', 'Nazwa klienta', 'Adres', 'Status', 'Suma'))

        for query in queryset:
            record = []
            for field in ('id', 'client_name', 'address', 'status', self.get_total_price):
                if hasattr(field, '__call__'):
                    item = field(query)
                else:
                    item = getattr(query, field, '')
                record.append(item)
            writer.writerow(record)
        return response

admin.site.register(Order, OrderAdmin)
