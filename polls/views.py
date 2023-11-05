from django.shortcuts import render, redirect
from django.template import Template, Context
import os
from django.http import HttpResponse
from .forms import RegistroForm
from .models import User

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
    print("Vistaqla")
    if request.method == 'POST':
        print("Test")
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario en la base de datos
            success = True  # Configura success en True para mostrar el mensaje de éxito
            return render(request, 'registro.html', {'success': success})
            print("Formulario válido, datos guardados")
            return redirect('login')
        else:
            print(form.errors)  # Esto mostrará los errores del formulario en la consola del servidor
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})


    #return render(request, 'registro.html', {'form': form})
# Create your views here.
