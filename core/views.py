from django.shortcuts import render, HttpResponse, redirect
from django.db import migrations, models
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
#def nome_evento(requests):
    #titulo_evento = evento.titulo
    #local = Evento.objects.all()
    #return local

def login_user(request):
    return render(request,'login.html')
def logout_user(request):
    logout(request)
    return redirect('/')

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

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento (request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        local_evento = request.POST.get('local_evento')
        usuario = request.user
        Evento.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)
    return redirect('/')
#def index(request):
   # return redirect('/agenda/')
