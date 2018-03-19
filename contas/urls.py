from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
from  contas import views

urlpatterns = [
    path('', auth_views.login, 
        {'template_name': 'login.html'}, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path(r'^sair/$', logout, {'template_name': 'login.html', 'next_page': '/'}, name='logout'),
    #path('', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
]