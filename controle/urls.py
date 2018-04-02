from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    # path(r'^produto/(?P<pk>[0-9]+)/$', views.produto_detalhe, name='produto_detalhe'),
    path('produto/<int:pk>/', views.produto_detalhe, name='produto_detalhe'),
    path('produto_novo/', views.produto_novo, name='produto_novo'),
    path('produto_editar/', views.produto_editar, name='produto_editar'),
    
    path('vendas/', views.vendas, name='vendas'),
    path('clientes/', views.clientes, name='clientes'),

]