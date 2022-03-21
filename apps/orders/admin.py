from pickle import ADDITEMS
from django.contrib import admin
from apps.orders.models import Address,OrderItem,Order,Payment

# Register your models here.
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)