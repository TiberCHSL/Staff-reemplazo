# Generated by Django 4.2.4 on 2023-11-14 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_alter_replacementrequest_ano_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='fecha_termino',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de término del estudio'),
        ),
        migrations.AlterField(
            model_name='replacementrequest',
            name='desc',
            field=models.TextField(verbose_name='Descripción del trabajo'),
        ),
    ]
