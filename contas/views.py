from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth import logout

from .forms import RegisterForm

def registrar(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
        
    else:
        form = RegisterForm()    
    context = {
        'form': form
    }
    return render(request, 'registrar.html', context)

def logout_view(request):
    logout(request)
    # Redirecione para uma página de sucesso.
