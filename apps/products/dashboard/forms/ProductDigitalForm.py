from django import forms
from apps.products.models.ProductDigital import ProductDigital, Products
from apps.core.mixins import Select2Mixin 

class ProductDigitalForm(Select2Mixin,forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(ProductDigitalForm, self).__init__(*args,**kwargs)
        self.fields['product'].queryset = Products.objects.filter(product_type='D')

    class Meta:
        model=ProductDigital
        fields=['id','product', 'code', 'link_redemption','is_active']

    def clean_product(self):
        product = self.cleaned_data['product']
        if product.product_type != 'D':
            raise forms.ValidationError("Este Producto no es Digital!!")
        return product

    def clean_code(self) -> str:
        code = self.cleaned_data['code'].strip()
        if 'code' in self.changed_data and self.Meta.model.objects.filter(code=code).exists():
            raise forms.ValidationError('El codigo Ingresado ya existe!!')
        return code
    
    def clean_link_redemption(self) -> str:
        link_redemption = self.cleaned_data['link_redemption']
        if 'link_redemption' in self.changed_data and self.Meta.model.objects.filter(link_redemption=link_redemption).exists():
            raise forms.ValidationError('El link del pdf ya existe Ingresado ya existe!!')
        return link_redemption

        