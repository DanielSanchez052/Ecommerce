from unicodedata import name
from django.urls import path
from apps.user.dashboard.views import CustomLogin
from django.contrib.auth.views import LogoutView
from apps.user.dashboard.forms import LoginFormCustom
from apps.user.dashboard import views 

urlpatterns = [
    path('login/', CustomLogin.as_view(
        redirect_authenticated_user = True, 
        template_name = 'accounts/login.html',
        authentication_form = LoginFormCustom
    ),name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name = "logout"), 

    #dashboard
    path('user-list/', views.UserView.as_view(), name='listUsers'),
    path('user-create/', views.UserCreate.as_view(), name='createUsers'),
    path('user-detail/<slug:username>/', views.UserDetailView.as_view(), name='detailUsers'),
    path('user-update/<int:pk>/', views.UserUpdate.as_view(), name='updateUser'),
    path('user-delete/<int:pk>/', views.UserDelete.as_view(), name='deleteUser'),
]
