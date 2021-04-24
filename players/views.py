from games.models import Game
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.shortcuts import render

from .models import Player


class PlayerListView(ListView):
    model = Player
    context_object_name = 'players'
    template_name = 'players/list.html'


def dashboard(request):
    results = Game.objects.filter(played=True)
    players = Player.objects.all()

    return render(request, 'players/dashboard.html', {
        'results': results,
        'players': players,
    })