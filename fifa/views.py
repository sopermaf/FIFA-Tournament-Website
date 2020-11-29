from django.shortcuts import render
from .models import Player, Game, Team


def dashboard(request):
    players = Player.objects.all()
    return render(
        request, 'fifa/dashboard.html', {'players': players}
    )
