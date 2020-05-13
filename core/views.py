from django.shortcuts import render, HttpResponse, redirect
from django.db import migrations, models
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def nome_evento(requests):
    titulo_evento = evento.titulo
    local = Evento.objects.all()
    return local

def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,'Usuário ou Senha inválidos')
    return redirect('/')

@login_required(login_url='/login/')
def lista_evento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario = usuario)
    dados = {'eventos':evento}
    return render(request,'agenda.html',dados)

def login_user(request):
    return render(request,'login.html')
def logout_user(request):
    logout(request)
    return redirect('/')

#def index(request):
   # return redirect('/agenda/')
