from django.shortcuts import render
from django.http import JsonResponse
from .models import Player
import json


def index(request):
    players = Player.objects.values('name', 'wins', 
              'draws', 'losses', 'points', 'goals_scored',
              'goals_against')

    context = {
        "page_data": json.dumps({'players': list(players)}),
    }
    return render(request, "app.html", context)
