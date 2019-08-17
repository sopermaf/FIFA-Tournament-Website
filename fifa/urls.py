from django.urls import path
from . import views

urlpatterns = [
    path('league/', views.index),
    path('data/', views.dataEntry),
    path('input/<str:player1>/<int:goals1>/<str:player2>/<int:goals2>/', views.addFixtureResult),
    path('playerInput/<str:player_name>/<str:password>/', views.playerTeamSelectionData),
    path('selectTeam/<str:player_id>/<str:opponent_id>/<str:team_id>/', views.selectTeam),
    path('vote/<str:voter>/<str:vote_made>/', views.makeVote),
    path('fixtures/', views.viewFixtures),
    path('players/', views.viewPlayers),
    path('', views.homepage),
    path('history/', views.historypage),
    path('create/<str:player1>/<str:player2>/<int:tv>/<str:time>', views.createFixture),
]
