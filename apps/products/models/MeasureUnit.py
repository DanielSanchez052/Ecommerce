from django.db import models
from apps.core.models import BaseModel

# Create your models here.

class MeasureUnit(BaseModel):
    description = models.CharField('Descripción', max_length=50,blank = False,null = False,unique = True)

    class Meta:

        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'

    def __str__(self):
        return self.description