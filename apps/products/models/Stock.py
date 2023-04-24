from typing import Dict
from django.db import models
from django.core.exceptions import ValidationError
from .Products import Products
from apps.core.models import BaseModel

class StockManager(models.Manager):

    def get_stock_inventory(self, *args, **kwargs) -> Dict[str,int]:
        inventory = self.aggregate(total_inventory = models.Sum('inventory'))
        return {'total_inventory': 0} if inventory['total_inventory'] == None else inventory

    def get_stock_available(self) -> Dict[str,int]:
        available = self.aggregate(total_available = models.Sum('available'))
        return {'total_available': 0} if available['total_available'] == None else available

    def get_stock_redemptions(self) -> int:
        return self.get_stock_inventory()['total_inventory'] - self.get_stock_available()['total_available']

class Stock(BaseModel):
    product = models.OneToOneField(Products, on_delete=models.CASCADE,verbose_name='Product', related_name='stock')
    inventory = models.PositiveIntegerField('inventario', blank=False, null=False)
    available = models.PositiveIntegerField('disponible', blank=False, null=False) 

    manage = StockManager()

    @property
    def redemptions (self) -> int:
        return self.inventory - self.available
    
        
    def clean(self, *args, **kwargs):
        errors = {}
        if self.available > self.inventory:
            errors.update(
                {"available":"El disponible no puede ser mayor al inventario"}
            )
        
        if self.product.product_type != 'F':
            errors.update({
                "product":"Este Producto no es Fisico!!"
            })

        if len(errors) > 0:
            raise ValidationError(errors)

    def __str__(self) -> str:
        return f"{self.product.name} inventario: {self.inventory} disponible: {self.available}"

    class Meta:
        verbose_name_plural='Stock'