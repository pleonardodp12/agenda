from django.shortcuts import render, HttpResponse, redirect
from django.db import migrations, models
from core.models import Evento

# Create your views here.
def nome_evento(requests):
    titulo_evento = evento.titulo
    local = Evento.objects.all()
    return local

def lista_evento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario = usuario)
    dados = {'eventos':evento}
    return render(request,'agenda.html',dados)

#def index(request):
   # return redirect('/agenda/')
