from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams', views.get_teams, name='all_teams')
]