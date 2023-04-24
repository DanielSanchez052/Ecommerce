from django.db import models
from apps.orders.models import Order

class Payment(models.Model):
    PAYMENT_METHODS = (
            ('Paypal','Paypal'),
        )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    timestamp = models.DateField(auto_now_add=True)
    amount = models.FloatField()
    raw_response = models.TextField()

    def __str__(self) -> str:
        return f"{self.reference_number}"

    @property
    def reference_number(self) -> str:
        return f"PAYMENT--{self.order}--{self.pk}"

    