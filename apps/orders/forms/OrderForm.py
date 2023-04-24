from django import forms

from apps.orders.models import Order, Address
from apps.core.mixins import Select2Mixin

class OrderForm(Select2Mixin, forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields["billing_address"].queryset = Address.objects.filter(address_type = 'B')
        self.fields["address_address"].queryset = Address.objects.filter(address_type = 'S')

    class Meta:
        model = Order
        fields = ["user", "ordered_date","billing_address", "address_address","is_paid"] 