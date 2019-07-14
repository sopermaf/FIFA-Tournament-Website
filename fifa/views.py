from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Player, Fixture, FixtureSide
from .forms import NameForm
import json
from datetime import datetime


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
    # get players and save results
    p1 = Player.objects.get(name=player1)
    p1.updatePlayer(goals1, goals2)

    p2 = Player.objects.get(name=player2)
    p2.updatePlayer(goals2, goals1)

    #find Fixture and add details
    

    # save the results
    p1.save()
    p2.save()

    return HttpResponse("Result Added")


def addFixtureResult(request, player1, goals1, player2, goals2):
    # get players and save results
    p1 = Player.objects.get(name=player1)
    p1.updatePlayer(goals1, goals2)
    p1.save()

    p2 = Player.objects.get(name=player2)
    p2.updatePlayer(goals2, goals1)
    p2.save()

    # find Fixture
    all_fixtures = Fixture.objects.all()
    found_fixture = ""
    for fixture in all_fixtures:
        all_p = fixture.listPlayers()
        if [player1, player2] == all_p or [player2, player1] == all_p:
            found_fixture = fixture

    if found_fixture == "":
        raise Exception("Fixture Not Found")

    # update Fixture for Result and removal from Fixtures
    found_fixture.game_played = True
    found_fixture.date = datetime.now()
    found_fixture.save()

    for fs in found_fixture.fixtureSides.all():
        if fs.player.name == player1:
            fs.goals = goals1
        elif fs.player.name == player2:
            fs.goals = goals2
        else:
            raise Exception('Unknown player in player field')

        fs.save()

    return HttpResponse("Result Added")


def viewFixtures(request):
    fixtures_data = []
    results_data = []

    # gather Scheduled Fixtures data
    for fixture in Fixture.objects.filter(game_played=False):
        fixture_ind = {}
        fixture_ind['fixture_sides'] = []
        for fixtureSide in fixture.fixtureSides.all():
            fixtureSide_data = {}

            fixtureSide_data['player_id'] = fixtureSide.player.id
            fixtureSide_data['name'] = fixtureSide.player.name
            
            fixture_ind['fixture_sides'].append(fixtureSide_data)
            print("Added " + fixtureSide.player.name)
            print(fixture_ind)

        # add value to individual record
        fixture_ind['fixture_id'] = fixture.id
        #fixture_ind['fixture_sides'] = fixtureSide_data
        fixture_ind['timestamp'] = str(fixture.date)
        
        # add a Fixture to fixtures dict
        fixtures_data.append(fixture_ind)

    # gather Result data

    context = {
        "page_data": json.dumps({
            'fixtures': fixtures_data,
            }),
    }
    return render(request, "fixtures.html", context)
