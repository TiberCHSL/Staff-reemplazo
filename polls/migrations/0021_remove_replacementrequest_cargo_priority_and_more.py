# Generated by Django 4.2.4 on 2023-11-15 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_replacementrequest_ano_exp_priority_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replacementrequest',
            name='cargo_priority',
        ),
        migrations.RemoveField(
            model_name='replacementrequest',
            name='fecha_priority',
        ),
        migrations.RemoveField(
            model_name='replacementrequest',
            name='nombre_empresa_priority',
        ),
    ]