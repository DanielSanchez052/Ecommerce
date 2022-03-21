from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout
from apps.products.models.Stock import Stock, Products
from apps.core.mixins import Select2Mixin 

class StockForm(Select2Mixin,forms.ModelForm):
    class Meta:
        model=Stock
        fields=['product', 'available', 'inventory', 'is_active']

    def __init__(self,*args, **kwargs):
        super(StockForm, self).__init__(*args,**kwargs)
        self.fields['product'].queryset = Products.objects.filter(product_type='F')

    def clean_product(self):
            product = self.cleaned_data['product']
            if product.product_type != 'F':
                raise forms.ValidationError("Este Producto no es Fisico!!")
            return product
    
    