from django.urls import reverse, reverse_lazy
from django.views import generic
from django_tables2 import SingleTableView  
from apps.products.dashboard.tables import CategoryTable
from apps.products.models import Category
from apps.products.dashboard.forms import CategoryForm
from apps.core.mixins import MessageValidMixin
from apps.core.mixins import auth

class CategoryView(auth.RequireLoginMixin,SingleTableView):
    table_class = CategoryTable
    queryset = Category.objects.all()
    template_name = 'home/products/category.html'


class CategoryCreate(auth.RequireLoginMixin,MessageValidMixin, generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'detail/categoryDetail.html'
    success_url = reverse_lazy("products:categories")
    extra_context = {'action':'create'}


class CategoryDetailView(auth.RequireLoginMixin,generic.DetailView):
    template_name = 'detail/categoryDetail.html'
    model = Category
    form_class = CategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['form'] = self.form_class(instance=category)
        context['action'] = 'detail'
        context['urlDelete'] = reverse('products:categoryDelete', args=[category.id])
        return context


class CategoryUpdate(auth.RequireLoginMixin,MessageValidMixin, generic.UpdateView):
    model=Category
    template_name = None
    template_name='detail/categoryDetail.html'
    form_class = CategoryForm
    success_url = reverse_lazy("products:categories")
    extra_context = {'action':'detail'}


class CategoryDelete(auth.RequireLoginMixin,MessageValidMixin, generic.DeleteView):
    model = Category
    template_name = 'detail/categoryDetail.html'
    success_url = reverse_lazy("products:categories")
    extra_context = {'action':'detail'}