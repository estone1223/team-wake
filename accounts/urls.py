from typing import Tuple
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, redirect_to_login

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='accouts/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]