from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_view
from django.conf import settings
from apps.user.dashboard.views.CustomLogin import CustomLogin
from django.contrib.auth.views import LogoutView
from apps.user.dashboard.forms import LoginFormCustom,ResetPasswordCustomForm
from apps.user.dashboard import views 

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name = "logout"), 
]

urlpatterns += [
    path('login/', CustomLogin.as_view(
        redirect_authenticated_user = True, 
        template_name = 'accounts/login.html',
        authentication_form = LoginFormCustom
    ),name = 'login'),

    path('reset_password/', auth_view.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        form_class=ResetPasswordCustomForm,
        from_email=settings.EMAIL_HOST_USER,
        email_template_name='email/reset_password.html',
        success_url=reverse_lazy("users:password_reset_done")
    ), name = 'password_reset'),

    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
         success_url = reverse_lazy("users:password_reset_complete")
    ),  name='password_reset_confirm'),

    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete')

]