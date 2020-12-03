from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('team-choice/', views.select_team, name='select_team'),
]
