# Generated by Django 4.2.4 on 2023-11-15 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_remove_replacementrequest_cargo_priority_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replacementrequest',
            name='desc_priority',
        ),
    ]
