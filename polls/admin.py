# admin.py
from django.contrib import admin
from .models import Usuario, Experience, Education, Language, ReplacementRequest
#from .models import Usuario, Curriculum, ReplacementRequest 
#from .models import Usuario, Curriculum, ReplacementRequest # Importa los modelos adicionales

# Registrar el modelo User para que aparezca en el admin
admin.site.register(Usuario)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Language)
admin.site.register(ReplacementRequest)

# Registrar el modelo Curriculum para que aparezca en el admin
#@admin.register(Curriculum)
#class CurriculumAdmin(admin.ModelAdmin):
    #list_display = ('user', 'education', 'skills')  # Personalizar las columnas que deseas mostrar
    #search_fields = ('user__full_name', 'education', 'skills')  # Habilitar la búsqueda por estos campos

# Registrar el modelo ReplacementRequest para que aparezca en el admin
#@admin.register(ReplacementRequest)
#class ReplacementRequestAdmin(admin.ModelAdmin):
    #list_display = ('requested_by', 'date_needed', 'urgency_level')  # Personalizar las columnas que deseas mostrar
    #list_filter = ('urgency_level',)  # Habilitar filtros por nivel de urgencia
    #search_fields = ('requested_by__full_name', 'reason', 'skills_required')  # Habilitar la búsqueda por estos campos
