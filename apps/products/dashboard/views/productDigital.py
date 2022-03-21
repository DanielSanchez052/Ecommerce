from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django_tables2 import SingleTableView  
from apps.products.dashboard.tables import ProductDigitalTable 
from apps.products.models import ProductDigital
from apps.products.dashboard.forms import ProductDigitalForm
from apps.core.mixins import MessageValidMixin
from apps.core.mixins import auth

# Create your views here.

class ProductDigitalView(auth.RequireLoginMixin,SingleTableView):
    table_class = ProductDigitalTable
    queryset = ProductDigital.objects.all()
    template_name = 'home/products/productDigital.html'


class ProductDigitalCreate(auth.RequireLoginMixin,MessageValidMixin, generic.CreateView):
    model = ProductDigital
    form_class = ProductDigitalForm
    template_name = 'detail/productDigitalDetail.html'
    success_url = reverse_lazy("products:productDigital")
    extra_context = { 'action': 'create' }


class ProductDigitalUpdate(auth.RequireLoginMixin,MessageValidMixin,generic.UpdateView):
    model=ProductDigital
    template_name='detail/productDigitalDetail.html'
    form_class = ProductDigitalForm
    success_url = reverse_lazy("products:productDigital")
    extra_context = { 'action' : 'detail' }

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid() and not self.object.redeem:
            return self.form_valid(form)
        else:
            if self.object.redeem:
                self.invalid_message = "El codigo ya ha sido utilizado por lo tanto no se puede actualizar"
            return self.form_invalid(form)
        
class DigitalDetailView(auth.RequireLoginMixin,generic.DetailView):
    template_name='detail/productDigitalDetail.html'
    model = ProductDigital
    form_class = ProductDigitalForm 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['form'] = self.form_class(instance=product)
        context['action'] = 'detail'
        context['urlDelete'] = reverse('products:productDigitalDelete', args=[product.id])
        return context



class ProductDigitalDelete(auth.RequireLoginMixin,MessageValidMixin, generic.DeleteView):
    model = ProductDigital
    template_name='detail/productDigitalDetail.html'
    success_url = reverse_lazy("products:productDigital")
    extra_context = { 'action' : 'detail' }

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid() and not self.object.redeem:
            return self.form_valid(form)
        else:
            if self.object.redeem:
                self.invalid_message = "El codigo ya ha sido utilizado por lo tanto no se puede Eliminar"
            return self.form_invalid(form)
        