from django.urls import reverse, reverse_lazy
from django.views import generic
from django_tables2 import SingleTableView  
from apps.products.dashboard.tables import MeasureUnitTable
from apps.products.models import MeasureUnit
from apps.products.dashboard.forms import MeasureUnitForm
from apps.core.mixins import MessageValidMixin, auth

class MeasureUnitView(auth.RequireLoginMixin,SingleTableView):
    table_class = MeasureUnitTable
    queryset = MeasureUnit.objects.all()
    template_name = 'home/products/measureUnit.html'


class MeasureUnitCreate(auth.RequireLoginMixin,MessageValidMixin,generic.CreateView):
    model = MeasureUnit
    form_class = MeasureUnitForm
    template_name = 'detail/measureUnitDetail.html'
    success_url = reverse_lazy("products:measureUnits")
    extra_context = {'action':'create'}


class MeasureUnitDetailView(auth.RequireLoginMixin,generic.DetailView):
    template_name = 'detail/measureUnitDetail.html'
    model = MeasureUnit
    form_class = MeasureUnitForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        MeasureUnit = self.get_object()
        context['form'] = self.form_class(instance=MeasureUnit)
        context['action'] = 'detail'
        context['urlDelete'] = reverse('products:meaureUnitDelete', args=[MeasureUnit.id])
        return context


class MeasureUnitUpdate(auth.RequireLoginMixin,MessageValidMixin,generic.UpdateView):
    model=MeasureUnit
    template_name = None
    template_name='detail/measureUnitDetail.html'
    form_class = MeasureUnitForm
    success_url = reverse_lazy("products:measureUnits")
    extra_context = {'action':'detail'}


class MeasureUnitDelete(auth.RequireLoginMixin,MessageValidMixin,generic.DeleteView):
    model = MeasureUnit
    template_name='detail/measureUnitDetail.html'
    success_url = reverse_lazy("products:measureUnits")
    extra_context = {'action':'detail'}

