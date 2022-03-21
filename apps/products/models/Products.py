from django.db import models
from apps.core.models import BaseModel
from apps.products.models import Category, MeasureUnit
from django.urls import reverse

class Products(BaseModel):

    PRODUCT_TYPE=[
        ('F','Fisico'),
        ('D','Digital'),
    ]
    
    name = models.CharField('Name', max_length = 255, blank = False, null = False)
    slug = models.SlugField()
    description = models.TextField('description', max_length=255, blank= False, null=False)
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    discount = models.DecimalField('discount', max_digits=3, decimal_places=2, default=0)
    terms = models.TextField('term and conditions', max_length=255, blank= True, null=True)
    instructions = models.TextField('instructions', max_length=255, blank= True, null=True)
    cost = models.IntegerField('Cost', blank=False, null=False )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category product')
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
    image = models.URLField('product image', max_length=255, null=False, blank = False)
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE, default='D')
    iva = models.FloatField('IVA',blank=False, null=False, default=0)

    def __str__(self) -> str:
        return f"{self.name} - {self.category.description}"

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'

    def get_price(self):
        return self.price * (1+self.discount)
    
    def get_absolute_url(self):
        return reverse("products:productDetail", kwargs={"slug": self.slug})
    

    