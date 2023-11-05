from django.shortcuts import render, redirect
from django.template import Template, Context
import os
from django.http import HttpResponse
from .forms import RegistroForm

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
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario en la base de datos
            # Redirige al usuario a la página de inicio de sesión o confirmación
            return redirect('/login')  # Reemplaza '/login' con la ruta real
    else:
        form = RegistroForm()


    return render(request, 'registro.html', {'form': form})
# Create your views here.
