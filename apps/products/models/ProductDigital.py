from django.db import models
from django.core.exceptions import ValidationError

from apps.core.models import BaseModel
from .Products import Products

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
    link_redemption = models.CharField('link redemption', max_length=100, blank=True, null=True, unique=True)

    manage = DigitalManager()

    def __str__(self):
        return f'{self.product.name} codigo: {self.code} redimido: {self.redeem}'


    def clean(self):
        errors = {}
        if self.product.product_type != 'D':
            errors.update({
                "product":"Este Producto no es Digital!!"
            })

        code_count = ProductDigital.objects.filter(pk=self.id).count()
        if code_count > 0 and ProductDigital.objects.get(pk=self.id).redeem:
            errors.update({
                "redeem":"El codigo digital ya fue redimido por lo tanto no se puede modificar"
            })            

        if len(errors) > 0:
            raise ValidationError(errors)

    class Meta:
        verbose_name='ProductDigital'
        verbose_name_plural='ProductsDigital'
