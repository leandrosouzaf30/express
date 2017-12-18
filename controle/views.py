from django.shortcuts import render
from . models import Produto

def produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    template = 'produto/produtos.html'
    return render(request, template, context)
