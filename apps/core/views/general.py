from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Sum
from apps.core.forms import ContactForm
from django.contrib import messages
from apps.products.models import Products,ProductDigital
from apps.products.models import Stock
from apps.core.mixins import auth
from apps.core.tasks import taskLog


class HomeView(auth.RequireLoginMixin,generic.TemplateView):
    template_name='home/index.html'
    product_model = Products

    def get(self, request, *args, **kwargs):
        total_products = self.product_model.objects.all()
        total_inventory = Stock.manage.get_stock_inventory()['total_inventory'] + ProductDigital.manage.get_digital_inventory()
        total_available = Stock.manage.get_stock_available()['total_available'] + ProductDigital.manage.get_digital_available()
        total_redemptions = Stock.manage.get_stock_redemptions() + ProductDigital.manage.get_digital_redemptions()
        active_products = total_products.filter(is_active=True).count()
        inactive_products = total_products.filter(is_active=False).count()
        context = {
            "total_products":total_products.count(),
            "active_products": active_products ,
            "inactive_procts":inactive_products ,
            "total_inventory": total_inventory,
            "total_available": total_available,
            "total_redemptions": total_redemptions,
        }
        return render(request, self.template_name, context)


class ContactView(generic.FormView):
    template_name='home/contact.html'
    form_class = ContactForm
    
    def get_success_url(self) -> str:
        return reverse_lazy("core:contact")

    def form_valid(self, form) -> HttpResponse:
        message:dict = form.send_email()  
        messages.info(self.request, message)
        return super().form_valid(form)  



        