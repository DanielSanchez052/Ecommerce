from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout
from apps.products.models import Stock, Products
from apps.core.mixins import Select2Mixin 

class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['product', 'available', 'inventory', 'is_active']

    def __init__(self,*args, **kwargs):
        super(StockForm, self).__init__(*args,**kwargs)
        self.fields['product'].queryset = Products.objects.filter(product_type='F')

    