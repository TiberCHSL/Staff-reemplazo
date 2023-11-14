# Generated by Django 4.2.4 on 2023-11-14 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0008_alter_language_idioma'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplacementRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cargo', models.CharField(max_length=40)),
                ('carrera', models.CharField(blank=True, choices=[('Administración de Empresas e Ing. Asociadas', 'Administración de Empresas e Ing. Asociadas'), ('Administración Gastronómica', 'Administración Gastronómica'), ('Administración Turística y Hotelera', 'Administración Turística y Hotelera'), ('Contador Auditor', 'Contador Auditor'), ('Ingeniería Comercial', 'Ingeniería Comercial'), ('Ingeniería en Comercio Exterior', 'Ingeniería en Comercio Exterior'), ('Ingeniería en Control de Gestión', 'Ingeniería en Control de Gestión'), ('Ingeniería en Finanzas', 'Ingeniería en Finanzas'), ('Ingeniería en Logística', 'Ingeniería en Logística'), ('Ingeniería en Marketing', 'Ingeniería en Marketing'), ('Ingeniería en Recursos Humanos', 'Ingeniería en Recursos Humanos'), ('Agronomía', 'Agronomía'), ('Ingeniería Agrícola', 'Ingeniería Agrícola'), ('Ingeniería en Acuicultura y Pesca', 'Ingeniería en Acuicultura y Pesca'), ('Ingeniería Forestal', 'Ingeniería Forestal'), ('Medicina Veterinaria', 'Medicina Veterinaria'), ('Actuación y Teatro', 'Actuación y Teatro'), ('Arquitectura', 'Arquitectura'), ('Artes y Licenciatura en Artes', 'Artes y Licenciatura en Artes'), ('Comunicación Audiovisual y/o Multimedia', 'Comunicación Audiovisual y/o Multimedia'), ('Diseño de Ambientes e Interiores', 'Diseño de Ambientes e Interiores'), ('Diseño de Vestuario', 'Diseño de Vestuario'), ('Diseño', 'Diseño'), ('Diseño Gráfico', 'Diseño Gráfico'), ('Fotografía', 'Fotografía'), ('Música, Canto o Danza', 'Música, Canto o Danza'), ('Realizador de Cine y Televisión', 'Realizador de Cine y Televisión'), ('Analista Químico', 'Analista Químico'), ('Biología Marina y Ecología Marina', 'Biología Marina y Ecología Marina'), ('Bioquímica', 'Bioquímica'), ('Geografía', 'Geografía'), ('Geología', 'Geología'), ('Matemáticas y/o Estadísticas', 'Matemáticas y/o Estadísticas'), ('Química Ambiental', 'Química Ambiental'), ('Química, Licenciado en Química', 'Química, Licenciado en Química'), ('Administración Pública Antropología', 'Administración Pública Antropología'), ('Administración Pública', 'Administración Pública'), ('Ciencias Políticas', 'Ciencias Políticas'), ('Ingeniería en Gestión Pública', 'Ingeniería en Gestión Pública'), ('Orientación Familiar y Relaciones Humanas', 'Orientación Familiar y Relaciones Humanas'), ('Periodismo', 'Periodismo'), ('Psicología', 'Psicología'), ('Publicidad', 'Publicidad'), ('Relaciones Públicas', 'Relaciones Públicas'), ('Sociología', 'Sociología'), ('Trabajo Social', 'Trabajo Social'), ('Derecho', 'Derecho'), ('Pedagogía en Artes y Música', 'Pedagogía en Artes y Música'), ('Pedagogía en Ciencias', 'Pedagogía en Ciencias'), ('Pedagogía en Educación Básica', 'Pedagogía en Educación Básica'), ('Pedagogía en Educación de Párvulos', 'Pedagogía en Educación de Párvulos'), ('Pedagogía en Educación Diferencial', 'Pedagogía en Educación Diferencial'), ('Pedagogía en Educación Física', 'Pedagogía en Educación Física'), ('Pedagogía en Filosofía y Religión', 'Pedagogía en Filosofía y Religión'), ('Pedagogía en Historia, Geografía y Ciencias Sociales', 'Pedagogía en Historia, Geografía y Ciencias Sociales'), ('Pedagogía en Inglés', 'Pedagogía en Inglés'), ('Pedagogía en Lenguaje, Comunicación y/o Castellano', 'Pedagogía en Lenguaje, Comunicación y/o Castellano'), ('Pedagogía en Matemáticas y Computación', 'Pedagogía en Matemáticas y Computación'), ('Psicopedagogía', 'Psicopedagogía'), ('Bibliotecología', 'Bibliotecología'), ('Licenciatura en Letras y Literatura', 'Licenciatura en Letras y Literatura'), ('Enfermería', 'Enfermería'), ('Fonoaudiología', 'Fonoaudiología'), ('Kinesiología', 'Kinesiología'), ('Medicina', 'Medicina'), ('Nutrición y Dietética', 'Nutrición y Dietética'), ('Obstetricia y Puericultura', 'Obstetricia y Puericultura'), ('Odontología', 'Odontología'), ('Química y Farmacia', 'Química y Farmacia'), ('Tecnología Médica', 'Tecnología Médica'), ('Terapia Ocupacional', 'Terapia Ocupacional'), ('Construcción Civil', 'Construcción Civil'), ('Diseño Industrial', 'Diseño Industrial'), ('Ingeniería Civil Ambiental', 'Ingeniería Civil Ambiental'), ('Ingeniería Civil Eléctrica', 'Ingeniería Civil Eléctrica'), ('Ingeniería Civil Electrónica', 'Ingeniería Civil Electrónica'), ('Ingeniería Civil en Biotecnología y/o Bioingeniería', 'Ingeniería Civil en Biotecnología y/o Bioingeniería'), ('Ingeniería Civil en Computación e Informática', 'Ingeniería Civil en Computación e Informática'), ('Ingeniería Civil en Minas', 'Ingeniería Civil en Minas'), ('Ingeniería Civil en Obras Civiles', 'Ingeniería Civil en Obras Civiles'), ('Ingeniería Civil Industrial', 'Ingeniería Civil Industrial'), ('Ingeniería Civil Mecánica', 'Ingeniería Civil Mecánica'), ('Ingeniería Civil Metalúrgica', 'Ingeniería Civil Metalúrgica'), ('Ingeniería Civil Química', 'Ingeniería Civil Química'), ('Ingeniería Civil, plan común y licenciatura en Ciencias de la Ingeniería', 'Ingeniería Civil, plan común y licenciatura en Ciencias de la Ingeniería'), ('Ingeniería en Alimentos', 'Ingeniería en Alimentos'), ('Ingeniería en Automatización, Instrumentación y Control', 'Ingeniería en Automatización, Instrumentación y Control'), ('Ingeniería en Biotecnología y Bioingeniería', 'Ingeniería en Biotecnología y Bioingeniería'), ('Ingeniería en Computación e Informática', 'Ingeniería en Computación e Informática'), ('Ingeniería en Conectividad y Redes', 'Ingeniería en Conectividad y Redes'), ('Ingeniería en Construcción', 'Ingeniería en Construcción'), ('Ingeniería en Electricidad', 'Ingeniería en Electricidad'), ('Ingeniería en Electrónica', 'Ingeniería en Electrónica'), ('Ingeniería en Geomensura y Cartografía', 'Ingeniería en Geomensura y Cartografía'), ('Ingeniería en Matemática y Estadística', 'Ingeniería en Matemática y Estadística'), ('Ingeniería en Mecánica Automotriz', 'Ingeniería en Mecánica Automotriz'), ('Ingeniería en Medio Ambiente', 'Ingeniería en Medio Ambiente'), ('Ingeniería en Minas y Metalurgia', 'Ingeniería en Minas y Metalurgia'), ('Ingeniería en Prevención de Riesgos', 'Ingeniería en Prevención de Riesgos'), ('Ingeniería en Química', 'Ingeniería en Química'), ('Ingeniería en Recursos Renovables', 'Ingeniería en Recursos Renovables'), ('Ingeniería en Sonido', 'Ingeniería en Sonido'), ('Ingeniería en Telecomunicaciones', 'Ingeniería en Telecomunicaciones'), ('Ingeniería en Transporte y Tránsito', 'Ingeniería en Transporte y Tránsito'), ('Ingeniería Industrial', 'Ingeniería Industrial'), ('Ingeniería Marina y Marítimo Portuaria', 'Ingeniería Marina y Marítimo Portuaria'), ('Ingeniería Mecánica', 'Ingeniería Mecánica')], max_length=100, null=True)),
                ('ano_exp', models.IntegerField()),
                ('idioma_requerido', models.CharField(blank=True, choices=[('IN', 'Ingles'), ('FR', 'Frances'), ('PO', 'Portugués'), ('AL', 'Alemán'), ('IT', 'Italiano')], max_length=30, null=True, verbose_name='Idioma')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Empleador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]