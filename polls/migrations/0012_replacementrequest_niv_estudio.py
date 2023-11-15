# Generated by Django 4.2.4 on 2023-11-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_replacementrequest_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='replacementrequest',
            name='niv_estudio',
            field=models.CharField(choices=[('S', 'Secundario'), ('T', 'Terciario'), ('U', 'Universitario'), ('P', 'Posgrado'), ('M', 'Master'), ('D', 'Doctorado'), ('O', 'Otro')], default='S', max_length=30, verbose_name='Nivel de estudio'),
            preserve_default=False,
        ),
    ]