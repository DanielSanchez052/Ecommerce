from urllib.parse import uses_query
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from apps.user.models import User

class LoginFormCustom(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class RegisterForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email","name", "last_name", "cellPhone", "password1", "password2", "is_staff", "groups","is_superuser"]


class ResetPasswordCustomForm(PasswordResetForm):
    username = forms.CharField(
        max_length=255,
        required=True, 
        widget=forms.TextInput(attrs={
                'autofocus': True,
                'autocapitalize': 'none',
                'autocomplete': 'username',
            }))

    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            })
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")

        userExists = User.objects.filter(username=username, email=email).exists()

        if not userExists:
            raise forms.ValidationError(
                "username or Email is not valid!",
                code="user invalid"
            )
        return self.cleaned_data