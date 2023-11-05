import datetime
from django.db import models
from django.utils import timezone



class User(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Nombre Completo")
    email = models.EmailField(verbose_name="Correo Electrónico")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    rut = models.CharField(primary_key = True,max_length=12, verbose_name="RUT")
    #verif = models.CharField(max_length=1, verbose_name="Digito verificador", choices=[('0', '0'),('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('K', 'K')])
    password = models.CharField(max_length=100, verbose_name="Contraseña")
    birth_date = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
    gender = models.CharField(max_length=10, verbose_name="Género", choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"



#class Choice(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)
    #def __str__(self):
        #return self.choice_text
# Create your models here.
