# Generated by Django 4.2.4 on 2023-11-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_user_id_alter_user_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verif',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('K', 'K')], default='0', max_length=1, verbose_name='Digito verificador'),
            preserve_default=False,
        ),
    ]