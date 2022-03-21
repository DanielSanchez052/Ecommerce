from django_tables2 import tables, columns
from apps.products.models import Products

class ProductTable(tables.Table):
    id = columns.TemplateColumn(template_name='tables/actionProducts.html', extra_context={'label':"id"})
    class Meta:
        model=Products
        attrs = {
            "class":"table tablesorter"
        }
        sequence = ("id", "name", "cost","price","discount","category", "measure_unit", "product_type", "created_at", "is_active")
        exclude = ("modified_at", "deleted_at", "image", "instructions", "terms", "description")

