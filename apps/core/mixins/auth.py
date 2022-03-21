from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy


class RequireLoginMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect(settings.LOGIN_URL)