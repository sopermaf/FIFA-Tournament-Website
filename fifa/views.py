from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Player, Fixture, FixtureSide, Team
from .forms import NameForm
import json
from datetime import datetime


# aux funct
def getUnplayedOpponents(player_name):
    '''
    Returns a list of the opponents for unplayed games
    '''
    player = Player.objects.get(name=player_name)
    opponents = []

    # only show games that haven't been played
    all_fixtures = Fixture.objects.filter(game_played=False)
    for fixture in all_fixtures:
        all_p = fixture.listPlayers()
        if player.name in all_p and not fixture.getSide(player.name).team_chosen:
            opponent_index = (all_p.index(player.name) + 1) % 2
            opp = Player.objects.get(name=all_p[opponent_index])
            opp_values = {
                'name': opp.name,
                'id': opp.id
            }
            opponents.append(opp_values)

    return opponents


# view


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


def addFixtureResult(request, player1, goals1, player2, goals2):
    # find Fixture
    all_fixtures = Fixture.objects.filter(game_played=False)
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
            fs.setValues(goals1, goals2)
        elif fs.player.name == player2:
            fs.setValues(goals2, goals1)
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
            # print("Added " + fixtureSide.player.name)
            print(fixture_ind)

        # add value to individual record
        fixture_ind['fixture_id'] = fixture.id
        fixture_ind['timestamp'] = str(fixture.date)
        
        # add a Fixture to fixtures dict
        fixtures_data.append(fixture_ind)

    # gather Result data
    for result in Fixture.objects.filter(game_played=True):
        result_ind = {}
        result_ind['fixture_sides'] = []
        for fixtureSide in result.fixtureSides.all():
            fixtureSide_data = {}

            fixtureSide_data['player_id'] = fixtureSide.player.id
            fixtureSide_data['name'] = fixtureSide.player.name
            fixtureSide_data['team'] = fixtureSide.team.name
            fixtureSide_data['goals'] = fixtureSide.goals
            result_ind['fixture_sides'].append(fixtureSide_data)

        # add value to individual record
        result_ind['fixture_id'] = result.id
        result_ind['timestamp'] = str(result.date)

        # add a Fixture to fixtures dict
        results_data.append(result_ind)

    print('Fixtures: ' + str(fixtures_data))
    print('Results: ' + str(results_data))

    context = {
        "page_data": json.dumps({
            'fixtures': fixtures_data,
            'results': results_data,
            }),
    }
    return render(request, "fixtures.html", context)


def playerTeamSelectionData(request, player_name):
    player = Player.objects.get(name=player_name)
    unusedTeams = player.getUnusedTeams()
    opponents = list(Player.objects.exclude(name=player_name).values('name', 'id'))
    opponents = getUnplayedOpponents(player_name)

    context = {
        "page_data": json.dumps({
            'unusedTeams': unusedTeams,
            'opponents': opponents,
            'username': player.name,
            'userID': player.id,
            }),
    }
    return render(request, "playerteam.html", context)


def selectTeam(request, player_id, opponent_id, team_id):
    # find Fixture
    user = Player.objects.get(id=player_id)
    opponent = Player.objects.get(id=opponent_id)
    team = Team.objects.get(id=team_id)

    all_fixtures = Fixture.objects.filter(game_played=False)
    found_fixture = ""
    for fixture in all_fixtures:
        all_p = fixture.listPlayers()
        if user.name in all_p and opponent.name in all_p:
            found_fixture = fixture

    if found_fixture == "":
        raise Exception("Fixture Not Found")

    # update FixtureSide with new player Team
    fs = found_fixture.getSide(user.name)
    fs.team = team
    fs.team_chosen = True
    team.chosen = True
    
    fs.save()
    team.save()

    opponents = getUnplayedOpponents(user.name)
    teams = user.getUnusedTeams()
    data = {
        'opponents': opponents,
        'teams': teams,
    }
    # return json with teams updated
    
    return JsonResponse(data)


def viewPlayers(request):
    players = Player.objects.values(
        'id',
        'name',
        'tournament_appearances',
        'best_overall_finish',
        'best_league_finish',
        'tournament_favourite',
        'description',
    )
    players = list(players)

    for player in players:
        p = Player.objects.get(id=player['id'])
        player['teams_available'] = p.getUnplayedTeams()

    context = {
        "page_data": json.dumps({'players': players}),
    }
    return render(request, "profile.html", context)
