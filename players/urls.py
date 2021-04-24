from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "players"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('list/', views.PlayerListView.as_view(), name='player_list'),
    path('', views.dashboard, name='dashboard'),
]