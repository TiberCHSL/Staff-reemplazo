from django.shortcuts import render
from django.template import Template, Context

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    login = open("D:/La_U/unap/FLP/pagina/polls/Templates/login.html")
    template = Template(login.read())
    login.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def registro(request):
    registro = open("D:/La_U/unap/FLP/pagina/polls/Templates/Registro.html")
    template = Template(registro.read())
    registro.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)
# Create your views here.
