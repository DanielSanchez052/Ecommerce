from django_tables2 import tables, columns
from apps.products.models import MeasureUnit


class MeasureUnitTable(tables.Table):
    id = columns.TemplateColumn(template_name='tables/actionMeasureUnit.html', extra_context={'label':"id"})
    class Meta:
        model=MeasureUnit
        attrs = {
            "class":"table tablesorter"
        }
        sequence = ("id", "description", "created_at", "is_active")
        exclude = ("modified_at", "deleted_at")

