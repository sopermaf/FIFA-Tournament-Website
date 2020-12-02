from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, ListView

from .models import Player


class PlayerListView(ListView):
    model = Player
    context_object_name = 'players'
    template_name = 'players/list.html'
