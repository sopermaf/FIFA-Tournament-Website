from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('data/', views.dataEntry),
    path('input/<str:player1>/<int:goals1>/<str:player2>/<int:goals2>/', views.addFixtureResult),
    path('fixtures/', views.viewFixtures)
]
