from django_tables2 import tables, columns
from apps.products.models import ProductDigital


class ProductDigitalTable(tables.Table):
    id = columns.TemplateColumn(template_name='tables/actionProductDigital.html', extra_context={'label':"id"})
    class Meta:
        model=ProductDigital
        attrs = {
            "class":"table tablesorter"
        }
        sequence = ('id', 'product', 'code', 'link_redemption', 'is_active')
        exclude = ("modified_at", "deleted_at")

