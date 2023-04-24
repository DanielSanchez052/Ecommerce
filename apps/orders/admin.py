from pickle import ADDITEMS
from django.contrib import admin
from django.conf import settings

from apps.orders.models import Address,OrderItem,Order,Payment
from apps.orders.forms.OrderForm import OrderForm

class AddressInLine(admin.StackedInline):
    model = Address
    min_num = 1
    max_num = 4

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    min_num = 1
    max_num = settings.CART_ITEM_MAX_QUANTITY

# Register your models here.
@admin.register(Address) 
class AddressAdmin(admin.ModelAdmin): 
    list_display = ('user','address_line_1','address_line_2','city','zip_code','address_type','default')
    search_fields = ('user',)
    list_per_page = 1000

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "start_date","ordered_date","billing_address","address_address","item_count","total_price","is_paid")
    inlines = [
        OrderItemInline
    ]
    form = OrderForm
    list_per_page = 1000

@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ('id','order','product','price','quantity', 'total_price')
    list_per_page = 1000

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','order','payment_method','timestamp','amount')
    list_per_page = 1000
