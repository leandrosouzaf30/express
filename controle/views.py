from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . models import Produto
from . models import ItemVendido
from . models import Cliente
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm

@login_required
def produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    template_produtos = 'produto/produtos.html'
    return render(request, template_produtos, context)


@login_required
def produto_novo(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_novo')     
    else:
        form = ProdutoForm()    
    context = {
        'form': form
    }
    return render(request, 'produto/cad_produto.html', context)
    
# @login_required
# def produto_editar(request):
#     form = get_object_or_404(Produto, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=produto)
#         if form.is_valid():
#             form.save()
#             return redirect('detalhe_produto', pk=produto.pk)


    
@login_required
def vendas(request):
    vendas = ItemVendido.objects.all()
    context = {
        'vendas': vendas,

    }
    template_vendas = 'vendas/vendas.html'
    return render(request, template_vendas, context)

@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    template_clientes = 'clientes/clientes.html'
    return render(request, template_clientes, context)








