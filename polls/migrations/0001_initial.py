# Generated by Django 4.2.4 on 2023-11-12 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('full_name', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='RUT')),
                ('password', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=10, verbose_name='Género')),
                ('role', models.CharField(choices=[('P', 'Postulante'), ('E', 'Empleador')], max_length=10, verbose_name='Rol de usuario')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
