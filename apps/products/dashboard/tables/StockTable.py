from django_tables2 import tables, columns
from apps.products.models import Stock

class StockTable(tables.Table):
    id = columns.TemplateColumn(template_name='tables/actionStock.html', extra_context={'label':"id"})
    redemptions = columns.Column('redemptions')
    class Meta:
        model=Stock
        attrs = {
            "class":"table tablesorter"
        }
        sequence = ("id", "product", "inventory", "available","redemptions", "modified_at", "is_active")
        exclude = ("created_at", "deleted_at")

