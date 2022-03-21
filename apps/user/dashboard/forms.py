from django import forms
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