from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . models import Produto
from . models import ItemVendido
from . models import Cliente
from . models import Fornecedor
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm
from .forms import VendaForm


@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    template_clientes = 'clientes/clientes.html'
    return render(request, template_clientes, context)


@login_required
def fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    context = {
        'fornecedores': fornecedores
    }
    template_fornecedores = 'fornecedores/fornecedores.html'
    return render(request, template_fornecedores, context)

"""
Metodos referentes a Produtos
"""
@login_required
def produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    template_produtos = 'produto/produtos.html'
    return render(request, template_produtos, context)

@login_required
def produto_detalhe(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produto/detalhe_produto.html', {'produto': produto})


@login_required
def produto_novo(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('produto_detalhe', pk=produto.pk)     
    else:
        form = ProdutoForm()    
    context = {
        'form': form
    }
    template_produtos = 'produto/cad_produto.html'
    return render(request, template_produtos, context)
    
@login_required
def produto_editar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('produto_detalhe', pk=produto.pk)
    else:
        form = ProdutoForm(instance=produto)    
    context = {
        'form': form
    }
    template_produtos = 'produto/editar_produto.html'
    return render(request, template_produtos, context)

@login_required
def produto_deletar(request, pk):
    produto = Produto.objects.get(pk=pk).delete()
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    template_produtos = 'produto/produtos.html'
    return render(request, template_produtos, context) 
        
@login_required
def vendas(request):
    vendas = ItemVendido.objects.all()
    context = {
        'vendas': vendas,

    }
    template_vendas = 'vendas/vendas.html'
    return render(request, template_vendas, context)


@login_required
def venda_detalhe(request, pk):
    venda = get_object_or_404(ItemVendido, pk=pk)
    return render(request, 'vendas/detalhe_venda.html', {'venda': venda})

@login_required
def venda_nova(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            venda.save()
            return redirect('venda_detalhe', pk=venda.pk)     
    else:
        form = VendaForm()    
    context = {
        'form': form
    }
    template_vendas = 'vendas/cad_vendas.html'
    return render(request, template_vendas, context)

@login_required
def venda_editar(request, pk):
    venda = get_object_or_404(ItemVendido, pk=pk)
    if request.method == "POST":
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            venda = form.save(commit=False)
            venda.save()
            return redirect('venda_detalhe', pk=venda.pk)
    else:
        form = VendaForm(instance=venda)    
    context = {
        'form': form
    }
    template_vendas = 'vendas/editar_venda.html'
    return render(request, template_vendas, context)

@login_required
def venda_deletar(request, pk):
    venda = ItemVendido.objects.get(pk=pk).delete()
    return redirect('vendas') 








