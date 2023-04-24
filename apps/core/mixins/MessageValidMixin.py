from django.contrib import messages

class MessageValidMixin(object):
    valid_message = 'Operacion realizada con exito'
    invalid_message = 'Ocurrio al tratar realizar la operacion'

    def form_valid(self, form):
        messages.info(self.request, {"type":"success","message":self.valid_message})
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, {"type":"danger","message":self.invalid_message})
        return super().form_invalid(form)
