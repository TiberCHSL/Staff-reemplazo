# Generated by Django 4.2.4 on 2023-11-15 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_alter_replacementrequest_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='replacementrequest',
            name='ano_exp_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='replacementrequest',
            name='cargo_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='replacementrequest',
            name='carrera_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='replacementrequest',
            name='desc_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='replacementrequest',
            name='fecha_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='replacementrequest',
            name='gender_required_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='replacementrequest',
            name='idioma_requerido_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='replacementrequest',
            name='niv_estudio_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='replacementrequest',
            name='nombre_empresa_priority',
            field=models.IntegerField(default=1),
        ),
    ]
