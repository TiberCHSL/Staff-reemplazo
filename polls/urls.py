from django.urls import path
from .views import index, login, registro, CurriculumView, ReplacementRequestView, CandidateListView
from . import views
from .views import curriculum_list

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("registro/", registro, name="registro"),
    path('curriculum/', CurriculumView.as_view(), name='curriculum'),
    path('request-replacement/', ReplacementRequestView.as_view(), name='request-replacement'),
    path('candidates/', CandidateListView.as_view(), name='candidates-list'),
    path('postulante/', views.vista_postulante, name='vista_postulante'),
    path('empleador/', views.vista_empleador, name='vista_empleador'),
     path('curriculums/', curriculum_list, name='curriculum-list'),
]
