# forms.py
from django import forms
from .models import Usuario
from django.contrib.auth.models import User
#from .models import Usuario, Curriculum, ReplacementRequest

class UserRegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name',  'last_name', 'email', 'password']

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['phone', 'rut', 'birth_date', 'gender', 'role']


#class CurriculumForm(forms.ModelForm):
    #class Meta:
        #model = Curriculum
        #fields = ['resume', 'skills', 'experience', 'education', 'certifications']

#class ReplacementRequestForm(forms.ModelForm):
    #class Meta:
        #model = ReplacementRequest
        #fields = ['date_needed', 'reason', 'skills_required', 'urgency_level']
