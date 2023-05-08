from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib.admin.filters import RelatedFieldListFilter
from django.forms import BaseInlineFormSet

from apps.products.models import Products, Category, MeasureUnit, ProductDigital, Stock
from apps.products.forms.ProductDigitalForm import ProductDigitalForm
from apps.products.forms.StockForm import StockForm 
# Register your models here.


class DigitalFormset(BaseInlineFormSet):
    def clean(self):
        super(DigitalFormset, self).clean()

        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue

            data = form.cleaned_data
            current = data.get('id')
            if (data.get('DELETE') and current):
                code_count = ProductDigital.objects.filter(pk=current.id).count()   
                if (code_count > 0 and ProductDigital.objects.get(pk=current.id).redeem):
                    raise ValidationError("El codigo digital ya fue redimido por lo tanto no se puede modificar")

    def delete_existing(self, obj, commit=True):
        if commit:
            obj.is_active = False
            obj.save()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_active = True)


class StockInline(admin.StackedInline):
    model = Stock
    min_num = 1
    max_num = 1


class ProductDigitalInline(admin.StackedInline):
    model = ProductDigital
    formset = DigitalFormset
    min_num = 1
    max_num = 10
    extra = 0


@admin.register(MeasureUnit)
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id','description','is_active')
    list_per_page = 1000


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','description','is_active')
    list_per_page = 1000


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cost","price","discount","category", "measure_unit", "available","product_type", "created_at", "is_active")
    list_per_page = 1000


    def get_inlines(self, request, obj=None):
        if obj is not None:
            if obj.product_type == 'F' and StockInline not in self.inlines:
                if ProductDigitalInline  in self.inlines: self.inlines.remove(ProductDigitalInline)          
                self.inlines.append(StockInline)
            elif obj.product_type == 'D' and ProductDigitalInline not in self.inlines:
                if StockInline  in self.inlines: self.inlines.remove(StockInline)          
                self.inlines.append(ProductDigitalInline)
            
        return self.inlines


class OnlyDigitalFilter(RelatedFieldListFilter):
    def field_choices(self, field, request, model_admin):
        ordering = self.field_admin_ordering(field, request, model_admin)
        ch = field.get_choices(include_blank=False, ordering=ordering, limit_choices_to={"product_type":'D'})
        return ch


@admin.register(ProductDigital)
class ProductDigitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'product','code', 'redeem','redeem_date','link_redemption', 'is_active')
    form = ProductDigitalForm
    list_per_page = 1000
    search_fields = ('code', 'link_redemption')
    list_filter = ['redeem', 'is_active', ('product', OnlyDigitalFilter) 
    ]

    def delete_queryset(self, request, queryset):
        queryset.update(is_active = 0)

    def delete_model(self, request, obj):
        obj.is_active = 0
        obj.save()


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "inventory", "available","redemptions", "modified_at", "is_active")
    form = StockForm
    list_per_page = 1000
    
