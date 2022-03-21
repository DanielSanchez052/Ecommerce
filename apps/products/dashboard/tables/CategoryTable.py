from django_tables2 import tables, columns
from apps.products.models import Category


class CategoryTable(tables.Table):
    id = columns.TemplateColumn(template_name='tables/actionCategory.html', extra_context={'label':"id"})
    class Meta:
        model=Category
        attrs = {
            "class":"table tablesorter"
        }
        sequence = ("id", "description", "created_at", "is_active")
        exclude = ("modified_at", "deleted_at")

