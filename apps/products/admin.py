from django.contrib import admin
from apps.products.models import Products, Category, MeasureUnit, ProductDigital, Stock
# Register your models here.

class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id','description','is_active')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','description','is_active')

admin.site.register(MeasureUnit,MeasureUnitAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Products)
admin.site.register(ProductDigital)
admin.site.register(Stock)