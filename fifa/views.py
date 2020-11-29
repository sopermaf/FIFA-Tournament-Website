from django.shortcuts import render
from .models import Player, Game, Team


def leaderboard(request):
    players = Player.objects.all()
    return render(
        request, 'fifa/leaderboard.html', {'players': players}
    )
