from django import forms
from apps.products.models.ProductDigital import ProductDigital, Products
from apps.core.mixins import Select2Mixin 

class ProductDigitalForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(ProductDigitalForm, self).__init__(*args,**kwargs)
        self.fields['product'].queryset = Products.objects.filter(product_type='D')

    class Meta:
        model=ProductDigital
        fields=['id','product', 'code', 'link_redemption', 'redeem', 'redeem_date', 'is_active']
