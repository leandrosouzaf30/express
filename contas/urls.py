from django.urls import path
from django.contrib.auth import views as auth_views

from  contas import views

urlpatterns = [
    path('entrar/', auth_views.login, 
        {'template_name': 'login.html'}, name='login'),
]