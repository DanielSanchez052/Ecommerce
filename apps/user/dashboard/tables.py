from django_tables2 import tables, columns
from apps.user.models import User 


class UserTable(tables.Table):
    id = columns.TemplateColumn(template_name='tables/actionUser.html', extra_context={'label':"id"})
    class Meta:
        model=User
        attrs = {
            "class":"table tablesorter"
        }
        sequence = ("id", "username", "email", "name", "last_name", "cellPhone", "is_staff", "is_superuser","last_login","is_active")
        exclude = ("password", "image",)

