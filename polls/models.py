from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name = "usuario")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    rut = models.CharField(primary_key=True, max_length=12, verbose_name="RUT")
    birth_date = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
    gender = models.CharField(max_length=10, verbose_name="Género", choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    role = models.CharField(max_length=10, verbose_name="Rol de usuario", choices=[('P', 'Postulante'), ('E', 'Empleador')])

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.usuario.save()
#post_save.connect(create_user_profile, sender = User)
#post_save.connect(save_user_profile, sender = User)



# A continuación, el modelo Curriculum con el campo last_updated añadido

#class Curriculum(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #resume = models.FileField(upload_to='resumes/')
    #skills = models.TextField()
    #experience = models.TextField()
    #education = models.CharField(max_length=255)
    #certifications = models.CharField(max_length=255, blank=True)
    #last_updated = models.DateTimeField(default=timezone.now)  # Campo añadido

    #def save(self, *args, **kwargs):
        #self.last_updated = timezone.now()
        #super(Curriculum, self).save(*args, **kwargs)

    #def __str__(self):
        #return f"{self.user.full_name}'s Curriculum"

    #def get_absolute_url(self):
        #return reverse('curriculum-detail', kwargs={'pk': self.pk})#class Curriculum(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #resume = models.FileField(upload_to='resumes/')
    #skills = models.TextField()
    #experience = models.TextField()
    #education = models.CharField(max_length=255)
    #certifications = models.CharField(max_length=255, blank=True)
    #last_updated = models.DateTimeField(default=timezone.now)  # Campo añadido

    #def save(self, *args, **kwargs):
        #self.last_updated = timezone.now()
        #super(Curriculum, self).save(*args, **kwargs)

    #def __str__(self):
        #return f"{self.user.full_name}'s Curriculum"

    #def get_absolute_url(self):
        #return reverse('curriculum-detail', kwargs={'pk': self.pk})

#class ReplacementRequest(models.Model):
    #requested_by = models.ForeignKey(User, related_name='requested_replacements', on_delete=models.CASCADE)
    #date_needed = models.DateField()
    #reason = models.TextField()
    #skills_required = models.TextField()
    #urgency_level = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    #def __str__(self):
        #return f"Replacement request by {self.requested_by.full_name} for {self.date_needed}"

    #def get_absolute_url(self):
        #return reverse('replacement-request-detail', kwargs={'pk': self.pk})
