# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Education, Experience, Language, ReplacementRequest, Usuario

class UserRegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name',  'last_name', 'email', 'password']

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['phone', 'rut', 'birth_date', 'gender', 'role']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['niv_estudio', 'carrera', 'institucion', 'estado', 'fecha_inicio', 'fecha_termino']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['empresa', 'ano_exp', 'cargo', 'desc']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['idioma']


class ReplacementRequestForm(forms.ModelForm):
    class Meta:
        model = ReplacementRequest
        fields = ['fecha','nombre_empresa', 'cargo', 'carrera', 'ano_exp', 'idioma_requerido']

#class ReplacementRequestForm(forms.ModelForm):
    #class Meta:
        #model = ReplacementRequest
        #fields = ['date_needed', 'reason', 'skills_required', 'urgency_level']
