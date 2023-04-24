from django.contrib import admin

from apps.products.models import Products, Category, MeasureUnit, ProductDigital, Stock
from apps.products.forms.ProductDigitalForm import ProductDigitalForm
from apps.products.forms.StockForm import StockForm 
# Register your models here.

class StockInline(admin.StackedInline):
    model = Stock
    min_num = 1
    max_num = 1

class ProductDigitalInline(admin.StackedInline):
    model = ProductDigital
    min_num = 1
    max_num = 10

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
        if obj.product_type == 'F' and StockInline not in self.inlines:
            if ProductDigitalInline  in self.inlines: self.inlines.remove(ProductDigitalInline)          
            self.inlines.append(StockInline)
        elif obj.product_type == 'D' and ProductDigitalInline not in self.inlines:
            if StockInline  in self.inlines: self.inlines.remove(StockInline)          
            self.inlines.append(ProductDigitalInline)
        
        return self.inlines
             
@admin.register(ProductDigital)
class ProductDigitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'code', 'redeem','redeem_date','link_redemption', 'is_active')
    form = ProductDigitalForm
    list_per_page = 1000


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "inventory", "available","redemptions", "modified_at", "is_active")
    form = StockForm
    list_per_page = 1000
    
