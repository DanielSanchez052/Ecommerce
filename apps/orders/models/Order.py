from django.db import models

from apps.core.validators import ValidateType
from apps.core.models import BaseModel
from apps.user.models import User
from apps.orders.models.Address import Address

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    ordered_date = models.DateField(blank=True, null=True)
    billing_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name="billing_address",blank=True, null=True, validators=[
        ValidateType(Address,'address_type', 'B')
    ])
    address_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name="shipping_address",blank=True, null=True, validators=[
        ValidateType(Address,'address_type', 'S')
    ])
    is_paid = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"{self.reference_number}" 

    @property
    def reference_number(self) -> str:
        return f"ORDER--{self.pk}"

    @property 
    def total_price(self):
        total_cost = sum(item.total_price for item in self.items.all())
        return total_cost
    
    @property
    def description(self):
        return ", ".join(
            [f"{item.quantity}x {item.product.name}" for item in self.items.all()]
        )

    @property
    def item_count(self):
        return self.items.count()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ("-created_at",)


