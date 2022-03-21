from django import forms
from apps.products.models.Category import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['description', 'slug','is_active']
