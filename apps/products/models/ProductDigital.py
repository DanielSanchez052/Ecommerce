from django.db import models
from apps.core.models import BaseModel
from apps.products.models.Products import Products

class DigitalManager(models.Manager):
    def get_digital_inventory(self):
        return self.all().count()

    def get_digital_available(self):
        return self.filter(redeem=False).count() 

    def get_digital_redemptions(self):
        return self.filter(redeem=True).count() 
        

class ProductDigital(BaseModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Product', related_name='productdigital')
    redeem = models.BooleanField('redeemed',default=False, blank=True, null=True)
    redeem_date = models.DateField('redeemed date', auto_now=False, auto_now_add=False, blank=True, null=True)
    code = models.CharField('code', max_length=100, blank=False, null=False, unique=True)
    link_redemption = models.CharField('link redemption', max_length=100, blank=True, null=True)

    manage = DigitalManager()

    def __str__(self):
        return f'{self.product.name} codigo: {self.code} redimido: {self.redeem}'

    class Meta:
        verbose_name='ProductDigital'
        verbose_name_plural='ProductsDigital'
