from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import logout

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
        else:
            return HttpResponse('Não cadastrado')
    else:
        form = UserCreationForm()    
    context = {
        'form': form
    }
    return render(request, 'registrar.html', context)

def logout_view(request):
    logout(request)
    # Redirecione para uma página de sucesso.
