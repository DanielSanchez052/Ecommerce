from django import forms
from apps.products.models.MeasureUnit import MeasureUnit 

class MeasureUnitForm(forms.ModelForm):
    class Meta:
        model=MeasureUnit
        fields=['description', 'is_active']
