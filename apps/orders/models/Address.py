from django.db import models
from apps.user.models import User

class Address(models.Model):
    ADDRESS_CHOICES=(
        ('B','Billing'),
        ('S','Shipping'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.zip_code}"

    class Meta:
        verbose_name='Address'
        verbose_name_plural='addresses'
        
