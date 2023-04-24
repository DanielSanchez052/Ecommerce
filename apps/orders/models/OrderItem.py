from django.conf import settings
from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.products.models import Products
from apps.orders.models import Order

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Products,related_name="order_items", on_delete=models.CASCADE, verbose_name='product')
    price = models.DecimalField("price", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(settings.CART_ITEM_MAX_QUANTITY)
    ])


    def __str__(self) -> str:
        return f"{self.quantity} x {self.product.name}"

    

    @property
    def total_price(self):
        return self.price * self.quantity 

    class Meta:
        verbose_name='OrderItem'
        verbose_name_plural='OrderItems'
