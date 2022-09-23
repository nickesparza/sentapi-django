from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams', views.get_teams, name='all_teams'),
    path('teams/<int:team_id>/', views.show_team, name='show_team')
]