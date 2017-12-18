from django.shortcuts import render

from controle.models import Produto

def home(request):
    dados_produtos = Produto.objects.all()
    context = {
        'dados_produtos': dados_produtos
    }
    template_name = 'home.html'
    return render(request, template_name, context)

