from django import forms
from apps.products.models.Products import Products
from apps.core.mixins import Select2Mixin 

class ProductForm(Select2Mixin,forms.ModelForm):
    class Meta:
        model=Products
        fields=['name','slug','description','terms','instructions','cost', 'price','discount','category', 'measure_unit', 'image', 'product_type', 'is_active']

