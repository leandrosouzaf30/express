from django.urls import path

from . import views

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path('vendas/', views.vendas, name='vendas'),
    path('clientes/', views.clientes, name='clientes'),
]