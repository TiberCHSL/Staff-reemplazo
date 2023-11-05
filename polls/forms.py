from django import forms
from .models import User

class RegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone', 'rut', 'password', 'birth_date', 'gender']
