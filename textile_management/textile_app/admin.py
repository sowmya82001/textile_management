from django.contrib import admin
from .models import Retailer
from django.contrib import admin
from .models import Supplier, Manufacturer, Order, Payment

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

admin.site.register(Supplier)


admin.site.register(Retailer)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'retailer', 'product_name', 'quantity', 'status')
    list_filter = ('status',)
    search_fields = ('product_name', 'retailer__name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'status')
    list_filter = ('status',)
    search_fields = ('order__id',)