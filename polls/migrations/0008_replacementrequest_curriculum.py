# Generated by Django 4.2.7 on 2023-11-06 20:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplacementRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_needed', models.DateField()),
                ('reason', models.TextField()),
                ('skills_required', models.TextField()),
                ('urgency_level', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=50)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_replacements', to='polls.user')),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resumes/')),
                ('skills', models.TextField()),
                ('experience', models.TextField()),
                ('education', models.CharField(max_length=255)),
                ('certifications', models.CharField(blank=True, max_length=255)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
        ),
    ]
