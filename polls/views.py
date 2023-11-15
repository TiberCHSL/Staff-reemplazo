from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail  # Importamos la función de Django para enviar emails
from django.conf import settings  # Importamos la configuración de Django para usar las variables de configuración del correo electrónico
from .forms import RegistroForm, UserRegistroForm, EducationForm, ExperienceForm, LanguageForm, ReplacementRequestForm
from .models import User, ReplacementRequest, Usuario, Education, Experience, Language
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
    print("Current user:", request.user)
    replacement_requests = ReplacementRequest.objects.filter(user=request.user)
    print("Replacement requests:", replacement_requests)
    return render(request, 'empleador.html', {'replacement_requests': replacement_requests})

@login_required
def vista_postulante(request):
    # Tu lógica para la vista postulante va aquí
    return render(request, 'postulante.html')  # Asegúrate de que esta plantilla existe

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')



@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect('vista_postulante')
    else:
        form = EducationForm()
    return render(request, 'add_education.html', {'form': form})

@login_required
def add_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('vista_postulante')
    else:
        form = ExperienceForm()
    return render(request, 'add_experience.html', {'form': form})

@login_required
def add_language(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save(commit=False)
            language.user = request.user
            language.save()
            return redirect('vista_postulante')
    else:
        form = LanguageForm()
    return render(request, 'add_language.html', {'form': form})

@login_required
def experience_list(request):
    if request.method == 'POST':
        experience_id = request.POST.get('experience_id')
        if experience_id:
            User.Experience.objects.get(id=experience_id).delete()
        return redirect('experience_list')
    else:
        experiences = User.Experience.objects.filter(user=request.user)
        return render(request, 'experience_list.html', {'experiences': experiences})
    
@login_required
def add_replacement_request(request):
    if request.method == 'POST':
        form = ReplacementRequestForm(request.POST)
        if form.is_valid():
            replacement_request = form.save(commit=False)
            replacement_request.user = request.user
            replacement_request.save()
            return redirect('vista_empleador')
    else:
        form = ReplacementRequestForm()
    return render(request, 'create_replacement_request.html', {'form': form})

@login_required
def delete_request(request, request_id):
    replacement_request = get_object_or_404(ReplacementRequest, id=request_id)
    replacement_request.delete()
    return redirect('vista_empleador')  # replace 'empleador' with the name of your empleador view

@login_required
def edit_replacement_request(request, pk):
    replacement_request = get_object_or_404(ReplacementRequest, pk=pk)
    if request.method == 'POST':
        form = ReplacementRequestForm(request.POST, instance=replacement_request)
        if form.is_valid():
            form.save()
            return redirect('vista_empleador')  # Reemplaza con la vista correspondiente
    else:
        form = ReplacementRequestForm(instance=replacement_request)
    return render(request, 'edit_replacement_request.html', {'form': form})

@login_required
def view_candidates(request, request_id):
    replacement_request = get_object_or_404(ReplacementRequest, id=request_id)
    candidates = User.objects.all() 

    # Get additional data for each candidate
    for candidate in candidates:
        usuario = Usuario.objects.get(user=candidate)
        educations = Education.objects.filter(user=candidate)
        experiences = Experience.objects.filter(user=candidate)
        languages = Language.objects.filter(user=candidate)

        # Add the additional data to the candidate object
        candidate.usuario = usuario
        candidate.educations = educations
        candidate.experiences = experiences
        candidate.languages = languages

        # Initialize score
        candidate.score = 1

        # Increment score based on matching attributes with the replacement request
        for education in educations:
            if replacement_request.niv_estudio == education.niv_estudio:
                candidate.score += 10 / replacement_request.niv_estudio_priority
            if replacement_request.carrera == education.carrera:
                candidate.score += 10 / replacement_request.carrera_priority

        for experience in experiences:
            if replacement_request.cargo == experience.cargo:
                candidate.score += 10 / replacement_request.cargo_priority
            if replacement_request.ano_exp <= experience.ano_exp:
                candidate.score += (experience.ano_exp - replacement_request.ano_exp) / replacement_request.ano_exp_priority

        for language in languages:
            if replacement_request.idioma_requerido == language.idioma:
                candidate.score += 10 / replacement_request.idioma_requerido_priority

        if replacement_request.gender_required == usuario.gender:
            candidate.score += 10 / replacement_request.gender_required_priority

    # Sort candidates by score in descending order
    candidates = sorted(candidates, key=lambda candidate: candidate.score, reverse=True)

    return render(request, 'candidates.html', {'candidates': candidates})