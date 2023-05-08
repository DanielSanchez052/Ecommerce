from django import forms

from apps.products.models.ProductDigital import ProductDigital, Products

class ProductDigitalForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(ProductDigitalForm, self).__init__(*args,**kwargs)
        self.fields['product'].queryset = Products.objects.filter(product_type='D')

    class Meta:
        model=ProductDigital
        fields=['id','product', 'code', 'link_redemption', 'redeem', 'redeem_date', 'is_active']

    def clean(self):
        cleanned_data = super().clean()
        current = self.instance

        code_count = ProductDigital.objects.filter(pk=current.id).count()
        if code_count > 0 and ProductDigital.objects.get(pk=current.id).redeem:
            raise forms.ValidationError("El codigo digital ya fue redimido por lo tanto no se puede modificar")
        return cleanned_data

