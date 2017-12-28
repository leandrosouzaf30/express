from django.shortcuts import render
from . models import Produto
from . models import ItemVendido
from . models import Cliente


def produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    template_produtos = 'produto/produtos.html'
    return render(request, template_produtos, context)
    

def vendas(request):
    vendas = ItemVendido.objects.all()
    context = {
        'vendas': vendas,

    }
    template_vendas = 'vendas/vendas.html'
    return render(request, template_vendas, context)

def clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    template_clientes = 'clientes/clientes.html'
    return render(request, template_clientes, context)





