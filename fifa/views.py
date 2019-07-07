from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Player
from .forms import NameForm
import json

def index(request):
    players = Player.objects.values('name', 'wins', 
              'draws', 'losses', 'points', 'goals_scored',
              'goals_against')

    context = {
        "page_data": json.dumps({'players': list(players)}),
    }
    return render(request, "app.html", context)


def dataEntry(request):
    players = Player.objects.values('name', 'wins', 
              'draws', 'losses', 'points', 'goals_scored',
              'goals_against')

    context = {
        "page_data": json.dumps({'players': list(players)}),
    }
    return render(request, "data.html", context)


def addResult(request, player1, goals1, player2, goals2):
    # get players
    p1 = Player.objects.get(name=player1)
    p2 = Player.objects.get(name=player2)

    # add goals scored and goals conceded
    p1.goals_scored += goals1
    p1.goals_against += goals2

    p2.goals_scored += goals2
    p2.goals_against += goals1

    # set points, wins, draws, losses
    if goals1 == goals2:
        p1.points += 1
        p2.points += 1

        p1.draws += 1
        p2.draws += 1
    elif goals1 > goals2:
        p1.points += 3

        p1.wins += 1
        p2.losses += 1
    elif goals2 > goals1:
        p2.points += 3

        p2.wins += 1
        p1.losses += 1
    

    # save the results
    p1.save()
    p2.save()

    return HttpResponse("Result Added")
