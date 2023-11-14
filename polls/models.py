from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name = "usuario")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    rut = models.CharField(primary_key=True, max_length=12, verbose_name="RUT")
    birth_date = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
    gender = models.CharField(max_length=10, verbose_name="Género", choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    role = models.CharField(max_length=10, verbose_name="Rol de usuario", choices=[('P', 'Postulante'), ('E', 'Empleador')])

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.usuario.save()
#post_save.connect(create_user_profile, sender = User)
#post_save.connect(save_user_profile, sender = User)



# A continuación, el modelo Curriculum con el campo last_updated añadido
CARRERA_CHOICES = [
    ('Administración de Empresas e Ing. Asociadas', 'Administración de Empresas e Ing. Asociadas'),
    ('Administración Gastronómica', 'Administración Gastronómica'),
    ('Administración Turística y Hotelera', 'Administración Turística y Hotelera'),
    ('Contador Auditor', 'Contador Auditor'),
    ('Ingeniería Comercial', 'Ingeniería Comercial'),
    ('Ingeniería en Comercio Exterior', 'Ingeniería en Comercio Exterior'),
    ('Ingeniería en Control de Gestión', 'Ingeniería en Control de Gestión'),
    ('Ingeniería en Finanzas', 'Ingeniería en Finanzas'),
    ('Ingeniería en Logística', 'Ingeniería en Logística'),
    ('Ingeniería en Marketing', 'Ingeniería en Marketing'),
    ('Ingeniería en Recursos Humanos', 'Ingeniería en Recursos Humanos'),
    ('Agronomía', 'Agronomía'),
    ('Ingeniería Agrícola', 'Ingeniería Agrícola'),
    ('Ingeniería en Acuicultura y Pesca', 'Ingeniería en Acuicultura y Pesca'),
    ('Ingeniería Forestal', 'Ingeniería Forestal'),
    ('Medicina Veterinaria', 'Medicina Veterinaria'),
    ('Actuación y Teatro', 'Actuación y Teatro'),
    ('Arquitectura', 'Arquitectura'),
    ('Artes y Licenciatura en Artes', 'Artes y Licenciatura en Artes'),
    ('Comunicación Audiovisual y/o Multimedia', 'Comunicación Audiovisual y/o Multimedia'),
    ('Diseño de Ambientes e Interiores', 'Diseño de Ambientes e Interiores'),
    ('Diseño de Vestuario', 'Diseño de Vestuario'),
    ('Diseño', 'Diseño'),
    ('Diseño Gráfico', 'Diseño Gráfico'),
    ('Fotografía', 'Fotografía'),
    ('Música, Canto o Danza', 'Música, Canto o Danza'),
    ('Realizador de Cine y Televisión', 'Realizador de Cine y Televisión'),
    ('Analista Químico', 'Analista Químico'),
    ('Biología Marina y Ecología Marina', 'Biología Marina y Ecología Marina'),
    ('Bioquímica', 'Bioquímica'),
    ('Geografía', 'Geografía'),
    ('Geología', 'Geología'),
    ('Matemáticas y/o Estadísticas', 'Matemáticas y/o Estadísticas'),
    ('Química Ambiental', 'Química Ambiental'),
    ('Química, Licenciado en Química', 'Química, Licenciado en Química'),
    ('Administración Pública Antropología', 'Administración Pública Antropología'),
    ('Administración Pública', 'Administración Pública'),
    ('Ciencias Políticas', 'Ciencias Políticas'),
    ('Ingeniería en Gestión Pública', 'Ingeniería en Gestión Pública'),
    ('Orientación Familiar y Relaciones Humanas', 'Orientación Familiar y Relaciones Humanas'),
    ('Periodismo', 'Periodismo'),
    ('Psicología', 'Psicología'),
    ('Publicidad', 'Publicidad'),
    ('Relaciones Públicas', 'Relaciones Públicas'),
    ('Sociología', 'Sociología'),
    ('Trabajo Social', 'Trabajo Social'),
    ('Derecho', 'Derecho'),
    ('Pedagogía en Artes y Música', 'Pedagogía en Artes y Música'),
    ('Pedagogía en Ciencias', 'Pedagogía en Ciencias'),
    ('Pedagogía en Educación Básica', 'Pedagogía en Educación Básica'),
    ('Pedagogía en Educación de Párvulos', 'Pedagogía en Educación de Párvulos'),
    ('Pedagogía en Educación Diferencial', 'Pedagogía en Educación Diferencial'),
    ('Pedagogía en Educación Física', 'Pedagogía en Educación Física'),
    ('Pedagogía en Filosofía y Religión', 'Pedagogía en Filosofía y Religión'),
    ('Pedagogía en Historia, Geografía y Ciencias Sociales', 'Pedagogía en Historia, Geografía y Ciencias Sociales'),
    ('Pedagogía en Inglés', 'Pedagogía en Inglés'),
    ('Pedagogía en Lenguaje, Comunicación y/o Castellano', 'Pedagogía en Lenguaje, Comunicación y/o Castellano'),
    ('Pedagogía en Matemáticas y Computación', 'Pedagogía en Matemáticas y Computación'),
    ('Psicopedagogía', 'Psicopedagogía'),
    ('Bibliotecología', 'Bibliotecología'),
    ('Licenciatura en Letras y Literatura', 'Licenciatura en Letras y Literatura'),
    ('Enfermería', 'Enfermería'),
    ('Fonoaudiología', 'Fonoaudiología'),
    ('Kinesiología', 'Kinesiología'),
    ('Medicina', 'Medicina'),
    ('Nutrición y Dietética', 'Nutrición y Dietética'),
    ('Obstetricia y Puericultura', 'Obstetricia y Puericultura'),
    ('Odontología', 'Odontología'),
    ('Química y Farmacia', 'Química y Farmacia'),
    ('Tecnología Médica', 'Tecnología Médica'),
    ('Terapia Ocupacional', 'Terapia Ocupacional'),
    ('Construcción Civil', 'Construcción Civil'),
    ('Diseño Industrial', 'Diseño Industrial'),
    ('Ingeniería Civil Ambiental', 'Ingeniería Civil Ambiental'),
    ('Ingeniería Civil Eléctrica', 'Ingeniería Civil Eléctrica'),
    ('Ingeniería Civil Electrónica', 'Ingeniería Civil Electrónica'),
    ('Ingeniería Civil en Biotecnología y/o Bioingeniería', 'Ingeniería Civil en Biotecnología y/o Bioingeniería'),
    ('Ingeniería Civil en Computación e Informática', 'Ingeniería Civil en Computación e Informática'),
    ('Ingeniería Civil en Minas', 'Ingeniería Civil en Minas'),
    ('Ingeniería Civil en Obras Civiles', 'Ingeniería Civil en Obras Civiles'),
    ('Ingeniería Civil Industrial', 'Ingeniería Civil Industrial'),
    ('Ingeniería Civil Mecánica', 'Ingeniería Civil Mecánica'),
    ('Ingeniería Civil Metalúrgica', 'Ingeniería Civil Metalúrgica'),
    ('Ingeniería Civil Química', 'Ingeniería Civil Química'),
    ('Ingeniería Civil, plan común y licenciatura en Ciencias de la Ingeniería', 'Ingeniería Civil, plan común y licenciatura en Ciencias de la Ingeniería'),
    ('Ingeniería en Alimentos', 'Ingeniería en Alimentos'),
    ('Ingeniería en Automatización, Instrumentación y Control', 'Ingeniería en Automatización, Instrumentación y Control'),
    ('Ingeniería en Biotecnología y Bioingeniería', 'Ingeniería en Biotecnología y Bioingeniería'),
    ('Ingeniería en Computación e Informática', 'Ingeniería en Computación e Informática'),
    ('Ingeniería en Conectividad y Redes', 'Ingeniería en Conectividad y Redes'),
    ('Ingeniería en Construcción', 'Ingeniería en Construcción'),
    ('Ingeniería en Electricidad', 'Ingeniería en Electricidad'),
    ('Ingeniería en Electrónica', 'Ingeniería en Electrónica'),
    ('Ingeniería en Geomensura y Cartografía', 'Ingeniería en Geomensura y Cartografía'),
    ('Ingeniería en Matemática y Estadística', 'Ingeniería en Matemática y Estadística'),
    ('Ingeniería en Mecánica Automotriz', 'Ingeniería en Mecánica Automotriz'),
    ('Ingeniería en Medio Ambiente', 'Ingeniería en Medio Ambiente'),
    ('Ingeniería en Minas y Metalurgia', 'Ingeniería en Minas y Metalurgia'),
    ('Ingeniería en Prevención de Riesgos', 'Ingeniería en Prevención de Riesgos'),
    ('Ingeniería en Química', 'Ingeniería en Química'),
    ('Ingeniería en Recursos Renovables', 'Ingeniería en Recursos Renovables'),
    ('Ingeniería en Sonido', 'Ingeniería en Sonido'),
    ('Ingeniería en Telecomunicaciones', 'Ingeniería en Telecomunicaciones'),
    ('Ingeniería en Transporte y Tránsito', 'Ingeniería en Transporte y Tránsito'),
    ('Ingeniería Industrial', 'Ingeniería Industrial'),
    ('Ingeniería Marina y Marítimo Portuaria', 'Ingeniería Marina y Marítimo Portuaria'),
    ('Ingeniería Mecánica', 'Ingeniería Mecánica'),
]

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    niv_estudio = models.CharField(max_length=30, verbose_name="Nivel de estudio", choices=[('S', 'Secundario'), ('T', 'Terciario'), ('U', 'Universitario'),('P', 'Posgrado'),('M', 'Master'),('D', 'Doctorado'),('O', 'Otro')])
    carrera = models.CharField(max_length=100, choices=CARRERA_CHOICES, null=True, blank=True)
    institucion = models.TextField(max_length = 40)
    estado = models.CharField(max_length=30, verbose_name="Estado del estudio", choices=[('E', 'En curso'),('G', 'Graduado'),('A', 'Abandonado')])
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio del estudio", null=True, blank=True)
    fecha_termino = models.DateField(verbose_name="Fecha de término del estudio", null=True, blank=True)

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length = 40)
    ano_exp = models.IntegerField()
    cargo = models.CharField(max_length = 30)
    desc = models.TextField(max_length = 200)
    #def save(self, *args, **kwargs):
        #self.last_updated = timezone.now()
        #super(Curriculum, self).save(*args, **kwargs)

IDIOMA_CHOICES = [
    ('IN', 'Ingles'),
    ('FR', 'Frances'),
    ('PO', 'Portugués'),
    ('AL', 'Alemán'),
    ('IT', 'Italiano'),
]
class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idioma = models.CharField(max_length=30, verbose_name="Idioma", choices=IDIOMA_CHOICES)

class ReplacementRequest(models.Model):
    user = models.ForeignKey(User, related_name='Empleador', on_delete=models.CASCADE)
    nombre_empresa = models.CharField(max_length=40)
    niv_estudio = models.CharField(max_length=30, verbose_name="Nivel de estudio requerido", choices=[('S', 'Secundario'), ('T', 'Terciario'), ('U', 'Universitario'),('P', 'Posgrado'),('M', 'Master'),('D', 'Doctorado'),('O', 'Otro')])
    fecha = models.DateField(verbose_name = "Fecha de inicio del trabajo")
    cargo = models.CharField(max_length=40, verbose_name = "Cargo del trabajo")
    carrera = models.CharField(max_length=100, verbose_name="Carrera requerida",choices=CARRERA_CHOICES, null=True, blank=True)
    ano_exp = models.IntegerField(verbose_name = "Años de experiencia requeridos")
    desc = models.TextField(verbose_name = "Descripción del trabajo")
    idioma_requerido = models.CharField(max_length=30, verbose_name="Idioma Requerido", choices=IDIOMA_CHOICES, null = True, blank = True)
    gender_required = models.CharField(max_length=10, verbose_name="Género Requerido", choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], null = True, blank = True)


#class PostulateView(models.Model):

    
    