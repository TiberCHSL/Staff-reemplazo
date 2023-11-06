# forms.py
from django import forms
from .models import User

class RegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone', 'rut', 'password', 'birth_date', 'gender', 'role']



# forms.py
from django import forms
from .models import Curriculum, ReplacementRequest

class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ['resume', 'skills', 'experience', 'education', 'certifications']

class ReplacementRequestForm(forms.ModelForm):
    class Meta:
        model = ReplacementRequest
        fields = ['date_needed', 'reason', 'skills_required', 'urgency_level']
