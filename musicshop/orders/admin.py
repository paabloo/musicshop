from django.contrib import admin
from musicshop.orders.models import Order, OrderProduct
from django.db.models import Count


class OrderProductAdminInline(admin.TabularInline):
    model = OrderProduct
    fk_name = 'order'


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderProductAdminInline, )
    list_display = ('client_name', 'address', 'status', 'get_total_price')
    fields = ('client_name', 'address', 'status', 'get_total_price')
    readonly_fields = ('get_total_price', )

    def get_total_price(self, obj):
        return sum(map(lambda p: p.product.price * p.quantity, obj.order_products.all()))
    get_total_price.short_description = 'total'

admin.site.register(Order, OrderAdmin)
