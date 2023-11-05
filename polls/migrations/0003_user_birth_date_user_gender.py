# Generated by Django 4.2.4 on 2023-11-04 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='M', max_length=10, verbose_name='Género'),
            preserve_default=False,
        ),
    ]