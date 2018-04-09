from django.urls import path, re_path
from . import views

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path('produto/<int:pk>/', views.produto_detalhe, name='produto_detalhe'),
    path('produto/cadastro/', views.produto_novo, name='produto_novo'),
    path('produto/<int:pk>/editar/', views.produto_editar, name='produto_editar'),
    path('produto/<int:pk>/excluir/', views.produto_deletar, name='produto_deletar'),
    
    path('vendas/', views.vendas, name='vendas'),
    path('clientes/', views.clientes, name='clientes'),

]