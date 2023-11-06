from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail  # Importamos la función de Django para enviar emails
from django.conf import settings  # Importamos la configuración de Django para usar las variables de configuración del correo electrónico
from .forms import CurriculumForm, ReplacementRequestForm, RegistroForm
from .models import Curriculum, ReplacementRequest, User
from django.views.generic import ListView


# Definir las vistas faltantes
def index(request):
    # Aquí iría la lógica de tu vista de inicio
    return render(request, 'index.html')  # Asegúrate de tener una plantilla 'index.html'

def login(request):
    # Aquí iría la lógica de tu vista de inicio de sesión
    return render(request, 'login.html')  # Asegúrate de tener una plantilla 'login.html'

def registro(request):
    form = RegistroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/login/')  # Redirige a la página de inicio de sesión después del registro
    return render(request, 'registro.html', {'form': form})  # Asegúrate de tener una plantilla 'registro.html'

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