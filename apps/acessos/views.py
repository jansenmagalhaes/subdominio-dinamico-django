from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.messages import constants
from .forms import AcessoForm

def entrar(request):
    acesso_form = AcessoForm(request)

    if request.method == 'POST':
        acesso_form = AcessoForm(request, data=request.POST)

        if acesso_form.is_valid():
            acesso_form.log_into(request)

            return redirect(reverse('home'))
        
    return render(request, 'acessos_entrar.html', {'acesso_form': acesso_form})

def sair(request):
    logout(request)

    messages.add_message(request, constants.SUCCESS, "Seu acesso foi encerrado.")

    return redirect(reverse('inicio'))