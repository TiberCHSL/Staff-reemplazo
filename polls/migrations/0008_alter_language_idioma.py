# Generated by Django 4.2.4 on 2023-11-13 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_language_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='idioma',
            field=models.CharField(choices=[('IN', 'Ingles'), ('FR', 'Frances'), ('PO', 'Portugués'), ('AL', 'Alemán'), ('IT', 'Italiano')], max_length=30, verbose_name='Idioma'),
        ),
    ]
