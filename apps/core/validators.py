from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError


def qs_filter(queryset, **kwargs):
    try:
        return queryset.filter(**kwargs)
    except (TypeError, ValueError, DataError):
        return queryset.none()

def qs_exists(queryset):
    try:
        return queryset.exists()
    except (TypeError, ValueError, DataError):
        return False

class ValidateType:
    message = "%(field_label)s type is invalid"
    code = "type_invalid"
    lookup = 'exact'
    
    def __init__(self, model, field_name, type_filter, queryset=None):
        self.model = model
        self.field_name = field_name
        self.queryset = self.model.objects.all()
        self.type_filter = type_filter

        if queryset:
            self.queryset = queryset

    def __call__(self, value):
        cleaned = self.clean(value)
        params = {"field_label":self.field_name}
        queryset = self.filter_queryset(value, self.field_name) 
        if not qs_exists(queryset):
            self.message = self.message.format(
                field=self.field_name, model=self.model)

            raise ValidationError(message=self.message,
                    code=self.code, params=params)

    def clean(self, data):
        return data

    def filter_queryset(self, value, field_name):
        filter = {'%s__%s' % ('pk', self.lookup): value,'%s' % (field_name):self.type_filter}
        return qs_filter(self.queryset, **filter)

