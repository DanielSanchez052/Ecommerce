from django.contrib.auth.views import LoginView
from apps.user.dashboard.forms import LoginFormCustom

# Create your views he
class CustomLogin(LoginView):
    form_class = LoginFormCustom

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as zmodified to force data updates/cookie to be saved.
            self.request.session.modified = True
            
        return super().form_valid(form)