from django.shortcuts import render
from . models import Produto
from . models import ItemVendido


def produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    template_produto = 'produto/produtos.html'
    return render(request, template_produto, context)
    

def vendas(request):
    vendas = ItemVendido.objects.all()
    context = {
        'vendas': vendas,

    }
    template_vendas = 'vendas/vendas.html'
    return render(request, template_vendas, context)


    


