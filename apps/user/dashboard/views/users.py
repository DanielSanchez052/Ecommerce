from django.urls import reverse, reverse_lazy
from django.views import generic
from django_tables2 import SingleTableView  
from apps.user.dashboard.tables import UserTable 
from apps.user.models import User
from apps.user.dashboard.forms import RegisterForm
from apps.core.mixins import MessageValidMixin, auth

class UserView(auth.RequireLoginMixin,SingleTableView):
    table_class = UserTable
    queryset = User.objects.all()
    template_name = 'accounts/users.html'


class UserCreate(auth.RequireLoginMixin,MessageValidMixin,generic.CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'detail/userDetail.html'
    success_url = reverse_lazy("users:listUsers")
    extra_context = {'action':'create'}


class UserDetailView(auth.RequireLoginMixin,generic.DetailView):
    template_name = 'detail/userDetail.html'
    model = User
    form_class = RegisterForm
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['form'] = self.form_class(instance=user)
        context['action'] = 'detail'
        context['urlDelete'] = reverse('users:deleteUser', args=[user.id])
        return context


class UserUpdate(auth.RequireLoginMixin,MessageValidMixin,generic.UpdateView):
    model=User
    template_name='detail/userDetail.html'
    form_class = RegisterForm
    success_url = reverse_lazy("users:listUsers")
    extra_context = {'action':'detail'}


class UserDelete(auth.RequireLoginMixin,MessageValidMixin,generic.DeleteView):
    model = User
    template_name='detail/userDetail.html'
    success_url = reverse_lazy("users:listUsers")
    extra_context = {'action':'detail'}

