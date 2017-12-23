from django.shortcuts import render

from controle.models import ItemVendido, Cliente, Produto, Fornecedor

def count_vendas(request):
    count_vendas = ItemVendido.objects.count()

def count_clientes(request):
    count_clientes = Cliente.objects.count()

def count_produtos(request):
    count_produtos = Produto.objects.count()

def count_fornecedores(request):
    count_fornecedores = Fornecedor.objects.count()

def home(request):
    
    context = {
        'count_vendas': ItemVendido.objects.count(),
        'count_clientes': Cliente.objects.count(),
        'count_produtos': Produto.objects.count(),
        'count_fornecedores': Fornecedor.objects.count()
    }
    template_name = 'home.html'
    return render(request, template_name, context)

