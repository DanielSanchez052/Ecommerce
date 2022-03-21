from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django_tables2 import SingleTableView  
from apps.products.dashboard.tables import StockTable 
from apps.products.models import Stock
from apps.products.dashboard.forms import StockForm
from apps.core.mixins import MessageValidMixin
from apps.core.mixins import auth

# Create your views here.

class StockView(auth.RequireLoginMixin,SingleTableView):
    table_class = StockTable
    queryset = Stock.objects.all()
    template_name = 'home/products/stock.html'

class StockCreate(auth.RequireLoginMixin,MessageValidMixin, generic.CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'detail/stockDetail.html'
    success_url = reverse_lazy("products:stock")
    extra_context = { 'action': 'create' }


class StockUpdate(auth.RequireLoginMixin,MessageValidMixin,generic.UpdateView):
    model=Stock
    template_name='detail/stockDetail.html'
    form_class = StockForm
    success_url = reverse_lazy("products:stock")
    extra_context = { 'action' : 'detail' }


class StockDetailView(auth.RequireLoginMixin,generic.DetailView):
    template_name='detail/stockDetail.html'
    model = Stock
    form_class = StockForm 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['form'] = self.form_class(instance=product)
        context['action'] = 'detail'
        context['urlDelete'] = reverse('products:stockDelete', args=[product.id])
        return context


class StockDelete(auth.RequireLoginMixin,MessageValidMixin,generic.DeleteView):
    model = Stock
    template_name='detail/stockDetail.html'
    success_url = reverse_lazy("products:stock")
    extra_context = { 'action' : 'detail' }