from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('data/', views.dataEntry),
    path('input/<str:player1>/<int:goals1>/<str:player2>/<int:goals2>/', views.addFixtureResult),
    path('playerInput/<str:player_name>/', views.playerTeamSelectionData),
    path('selectTeam/<str:player_id>/<str:opponent_id>/<str:team_id>/', views.selectTeam),
    path('fixtures/', views.viewFixtures)
]
