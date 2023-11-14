from django.urls import path
from .views import index, login, registro
#from .views import index, login, registro, CurriculumView, ReplacementRequestView, CandidateListView
from . import views
#from .views import curriculum_list
#from .views import (create_replacement_request, replacement_request_list,edit_replacement_request, cancel_replacement_request)
                    

urlpatterns = [
    path("", index, name="index"),
    #path("login/", login, name="login"),
    path("registro/", registro, name="registro"),
    #path('curriculum/', CurriculumView.as_view(), name='curriculum'),
    #path('request-replacement/', ReplacementRequestView.as_view(), name='request-replacement'),
    #path('candidates/', CandidateListView.as_view(), name='candidates-list'),
    path('postulante/', views.vista_postulante, name='vista_postulante'),
    path('empleador/', views.vista_empleador, name='vista_empleador'),
    path('logout/', views.logout_view, name='logout'),
    #path('curriculums/', curriculum_list, name='curriculum-list'),
    #path('replacement-requests/new/', create_replacement_request, name='create_replacement_request'),
    #path('replacement-requests/', replacement_request_list, name='replacement_request_list'),
    #path('replacement-requests/edit/<int:pk>/', edit_replacement_request, name='edit_replacement_request'),
    #path('replacement-requests/cancel/<int:pk>/', cancel_replacement_request, name='cancel_replacement_request'),
     #path('accounts/login/', views.login_view, name='login'),
    #path('polls/replacement-requests/new/', views.create_replacement_request, name='create_replacement_request'),
    #path('polls/replacement-requests/edit/<int:pk>/', views.edit_replacement_request, name='edit_replacement_request'),
    path('polls/education/add/', views.add_education, name='add_education'),
    path('polls/experience/add/', views.add_experience, name='add_experience'),
    path('polls/language/add/', views.add_language, name='add_language'),
    path('polls/replacement_request/add/', views.add_replacement_request, name='add_replacement_request'),
]
