from django.urls import path
from .views import index, login, registro, CurriculumView, ReplacementRequestView, CandidateListView


urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("registro/", registro, name="registro"),
    path('curriculum/', CurriculumView.as_view(), name='curriculum'),
    path('request-replacement/', ReplacementRequestView.as_view(), name='request-replacement'),
    path('candidates/', CandidateListView.as_view(), name='candidates-list'),
]
