from django.shortcuts import render
from django.template import Template, Context
import os
from django.http import HttpResponse

template_path = os.path.join('polls', 'Templates', 'login.html')
template_path2 = os.path.join('polls', 'Templates', 'Registro.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    with open(template_path, 'r') as template_file:
        template = Template(template_file.read())
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)



def registro(request):
    with open(template_path2, 'r') as template_file:
        template = Template(template_file.read())
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)
# Create your views here.
