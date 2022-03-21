from django.urls import reverse_lazy, reverse
from django.views import generic
from django_tables2 import SingleTableView  
from apps.products.dashboard.tables import ProductTable 
from apps.products.models import Products
from apps.products.dashboard.forms import ProductForm
from apps.core.mixins import MessageValidMixin
from apps.core.mixins import auth
# Create your views here.

class ProductsView(auth.RequireLoginMixin,SingleTableView):
    table_class = ProductTable
    queryset = Products.objects.all()
    template_name = 'home/products/products.html'

class ProductCreate(auth.RequireLoginMixin,MessageValidMixin, generic.CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'detail/productDetail.html'
    success_url = reverse_lazy("products:products")
    extra_context = { 'action': 'create' }


class ProductUpdate(auth.RequireLoginMixin,MessageValidMixin,generic.UpdateView):
    model=Products
    template_name='detail/productDetail.html'
    form_class = ProductForm
    success_url = reverse_lazy("products:products")
    extra_context = { 'action' : 'detail' }


class ProductDetailView(auth.RequireLoginMixin,generic.DetailView):
    template_name='detail/productDetail.html'
    model = Products
    form_class = ProductForm 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['form'] = self.form_class(instance=product)
        context['action'] = 'detail'
        context['urlDelete'] = reverse('products:productDelete', args=[product.id])
        return context


class ProductDelete(auth.RequireLoginMixin,MessageValidMixin,generic.DeleteView):
    model = Products
    template_name='detail/productDetail.html'
    success_url = reverse_lazy("products:products")
    extra_context = { 'action' : 'detail' }