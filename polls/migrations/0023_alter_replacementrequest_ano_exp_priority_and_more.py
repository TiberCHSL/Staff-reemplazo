# Generated by Django 4.2.4 on 2023-11-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_remove_replacementrequest_desc_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replacementrequest',
            name='ano_exp_priority',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='replacementrequest',
            name='carrera_priority',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='replacementrequest',
            name='gender_required_priority',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='replacementrequest',
            name='idioma_requerido_priority',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='replacementrequest',
            name='niv_estudio_priority',
            field=models.IntegerField(default=5),
        ),
    ]
