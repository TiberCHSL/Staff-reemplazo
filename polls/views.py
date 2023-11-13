from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail  # Importamos la función de Django para enviar emails
from django.conf import settings  # Importamos la configuración de Django para usar las variables de configuración del correo electrónico
from .forms import RegistroForm, UserRegistroForm
#from .forms import CurriculumForm, ReplacementRequestForm, RegistroForm
#from .models import Curriculum, ReplacementRequest, User
from .models import User
from django.contrib.auth.hashers import check_password, make_password
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
#from .forms import ReplacementRequestForm



# Definir las vistas faltantes
def index(request):
    # Aquí iría la lógica de tu vista de inicio
    return render(request, 'base.html')  # Asegúrate de tener una plantilla 'index.html'




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Usuario Autenticado")
            if user.usuario.role == 'P':
                return redirect('vista_postulante')
            elif user.usuario.role == 'E':
                return redirect('vista_empleador')
        else:
            print("Mensaje de error")
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def registro(request):
    if request.method == 'POST':
        user_form = UserRegistroForm(request.POST)
        registro_form = RegistroForm(request.POST)
        print(request.POST)
        if user_form.is_valid() and registro_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            print(user)
            user.save()
            usuario = registro_form.save(commit=False)
            usuario.user = user
            print(usuario)
            usuario.save()
            return redirect('/')  # replace 'success_url' with the name of the URL you want to redirect to
        else:
            print("User form errors:", user_form.errors)  # print User form errors
            print("Registro form errors:", registro_form.errors)  # print Registro form errors
    else:
        user_form = UserRegistroForm()
        registro_form = RegistroForm()
    return render(request, 'registro.html', {'user_form': user_form, 'registro_form': registro_form})


@login_required
def vista_empleador(request):
    # Aquí va la lógica de la vista para el empleador
    return render(request, 'empleador.html')  # Asegúrate de tener una plantilla 'empleador.html'

@login_required
def vista_postulante(request):
    # Tu lógica para la vista postulante va aquí
    return render(request, 'postulante.html')  # Asegúrate de que esta plantilla existe

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')




#class CurriculumView(LoginRequiredMixin, View):
    form_class = CurriculumForm
    initial = {'key': 'value'}
    template_name = 'curriculum_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            curriculum = form.save(commit=False)
            curriculum.user = request.user
            # Guardamos el currículum para que obtenga un 'id' y pueda ser usado en 'get_absolute_url'
            curriculum.save()
            # Enviamos el correo electrónico de notificación
            send_mail(
                'Actualización de Curriculum',
                'Tu currículum ha sido actualizado exitosamente.',
                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False,
            )
            return HttpResponseRedirect(curriculum.get_absolute_url())  # Redirigimos a la URL del currículum

        return render(request, self.template_name, {'form': form})
    
      
#class ReplacementRequestView(LoginRequiredMixin, View):
    form_class = ReplacementRequestForm
    initial = {'key': 'value'}
    template_name = 'replacement_request_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            replacement_request = form.save(commit=False)
            replacement_request.requested_by = request.user
            replacement_request.save()
            return HttpResponseRedirect('/thanks/')  # Asegúrate de tener una ruta para '/thanks/'

        return render(request, self.template_name, {'form': form})

# Vista de lista para Candidate
# Vista de lista para los usuarios que son candidatos
#class CandidateListView(LoginRequiredMixin, ListView):
    model = User  # Usamos el modelo User en lugar de Candidate
    context_object_name = 'candidates'
    template_name = 'candidate_list.html'
    paginate_by = 10  # Opcional: añade paginación si tienes muchos candidatos

    def get_queryset(self):
        # Filtra para obtener solo los usuarios que tienen el rol de candidato ('P' para postulante)
        return User.objects.filter(role='P')
    

    
    def curriculum_list(request):
        curriculums = Curriculum.objects.all()  # Obtiene todos los currículums de la base de datos
        return render(request, 'polls/curriculum_list.html', {'curriculums': curriculums})





#@login_required
#def create_replacement_request(request):
    if request.method == 'POST':
        form = ReplacementRequestForm(request.POST)
        if form.is_valid():
            replacement_request = form.save(commit=False)
            replacement_request.requested_by = request.user
            replacement_request.save()
            return redirect('replacement_request_list')
    else:
        form = ReplacementRequestForm()
    return render(request, 'create_replacement_request.html', {'form': form})

#@login_required
#def replacement_request_list(request):
    #requests = ReplacementRequest.objects.filter(requested_by=request.user)
    #return render(request, 'polls/replacement_request_list.html', {'requests': requests})

#@login_required
#def edit_replacement_request(request, pk):
    #replacement_request = get_object_or_404(ReplacementRequest, pk=pk, requested_by=request.user)
    #if request.method == 'POST':
        #form = ReplacementRequestForm(request.POST, instance=replacement_request)
        #if form.is_valid():
            #form.save()
            #return redirect('replacement_request_list')
    #else:
        #form = ReplacementRequestForm(instance=replacement_request)
    #return render(request,'replacement_request_form.html', {'form': form})

#@login_required
#def cancel_replacement_request(request, pk):
    #replacement_request = get_object_or_404(ReplacementRequest, pk=pk, requested_by=request.user)
    #replacement_request.delete()
    #return redirect('replacement_request_list')