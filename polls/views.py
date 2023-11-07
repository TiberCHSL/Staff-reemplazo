from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail  # Importamos la función de Django para enviar emails
from django.conf import settings  # Importamos la configuración de Django para usar las variables de configuración del correo electrónico
from .forms import CurriculumForm, ReplacementRequestForm, RegistroForm
from .models import Curriculum, ReplacementRequest, User
from django.views.generic import ListView
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect


# Definir las vistas faltantes
def index(request):
    # Aquí iría la lógica de tu vista de inicio
    return render(request, 'index.html')  # Asegúrate de tener una plantilla 'index.html'

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirecciona según el rol del usuario
            if user.role == 'E':
                return redirect('vista_empleador')
            elif user.role == 'P':
                return redirect('vista_postulante')
        else:
            # Devuelve un mensaje de error de inicio de sesión
            return render(request, 'login.html', {'error': 'Email o contraseña inválidos.'})
    else:
        return render(request, 'login.html')

def registro(request):
    form = RegistroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/login/')  # Redirige a la página de inicio de sesión después del registro
    return render(request, 'registro.html', {'form': form})  # Asegúrate de tener una plantilla 'registro.html'



def vista_empleador(request):
    # Aquí va la lógica de la vista para el empleador
    return render(request, 'empleador.html')  # Asegúrate de tener una plantilla 'empleador.html'

def vista_postulante(request):
    # Tu lógica para la vista postulante va aquí
    return render(request, 'postulante.html')  # Asegúrate de que esta plantilla existe




class CurriculumView(LoginRequiredMixin, View):
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
    
      
class ReplacementRequestView(LoginRequiredMixin, View):
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
class CandidateListView(LoginRequiredMixin, ListView):
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