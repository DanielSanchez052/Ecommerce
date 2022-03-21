from django.core.mail import send_mail
from django.conf import settings
from django import forms
from django.template.loader import render_to_string 
from django.utils.html import strip_tags

class ContactForm(forms.Form):
    name = forms.CharField(max_length='100', required=True ,widget=forms.TextInput(attrs={
        "placeholder":'Ingresa tu nombre'
    }))
    email = forms.EmailField(max_length='100', required=True,widget=forms.TextInput(attrs={
        "placeholder":'Ingresa tu Email'
    }))
    cellPhone = forms.CharField(max_length='15', required=False,widget=forms.TextInput(attrs={
        "placeholder":'Ingresa un  numero de telefono (opcional)'
    }))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "placeholder":'Ingresa el mensaje',
        "rows":'5'
    }))

    def send_email(self) -> dict: 
        try:
            cellphone = f", {self.cleaned_data.get('cellPhone')}" if self.cleaned_data.get('cellPhone') != '' else ''
            subject= f" mensaje de contacto {self.cleaned_data.get('name')}, {self.cleaned_data.get('email')}{cellphone}"
            context = {
                "name":self.cleaned_data.get('name'),
                "email": self.cleaned_data.get('email'),
                "cellphone": cellphone,
                "message":self.cleaned_data.get('message')
            } 

            html_message = render_to_string('email/index.html', context=context)
            plain_message = strip_tags(html_message) 
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=settings.EMAIL_NOTIFY,
                html_message=html_message
            )
            return {"type":"success","message":"mensaje enviado con exito"}
        except Exception as e:
            print(e.__class__)
            return {"type":"danger","message":"el mensaje no se ha enviado"}

