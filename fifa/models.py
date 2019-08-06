from django.db import models
from datetime import datetime as dt


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    chosen = models.BooleanField(default=False)
    played = models.BooleanField(default=False)
    star_rating = models.FloatField(default=0)

    def __str__(self):
        return 'id: ' +  str(self.id) + ', ' + self.name + ": " + str(self.chosen)


class Player(models.Model):
    # identity info
    name = models.CharField(max_length=200)
    teams = models.ManyToManyField(Team, null=True, blank=True)

    # player profile
    tournament_appearances = models.PositiveIntegerField(default=0)
    best_overall_finish = models.CharField(max_length=50, default="no overall finish", blank=True, null=True)
    best_league_finish = models.CharField(max_length=50, default="no league finish", blank=True, null=True)
    tournament_favourite = models.CharField(max_length=100, default="no favourite", blank=True, null=True)
    description = models.CharField(max_length=20000, default="no desc", blank=True, null=True)

    # statistics
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_against = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'id: ' +  str(self.id) + ', ' +self.name

    def allTeams(self):
       return self.teams.all()

    def getUnusedTeams(self):
        unusedTeams = self.teams.all().filter(chosen=False).values('id', 'name')
        return list(unusedTeams)

    def getUnplayedTeams(self):
        unplayedTeams = self.teams.all().filter(played=False).values('id', 'name', 'star_rating')
        return list(unplayedTeams)

    def calculateGamesPlayed(self):
        return self.wins + self.draws + self.losses

    def calculateGoalDiff(self):
        return self.goals_scored + self.goals_against

    def updatePlayer(self, myGoals, opponentGoals):
        self.goals_scored += myGoals
        self.goals_against += opponentGoals

        if myGoals == opponentGoals:
            self.points += 1
            self.draws += 1
        elif myGoals > opponentGoals:
            self.points += 3
            self.wins += 1
        elif myGoals < opponentGoals:
            self.losses += 1


class FixtureSide(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)
    goals = models.PositiveIntegerField(default=None, blank=True, null=True)
    team_chosen = models.BooleanField(default=False)

    def __str__(self):
        return 'id: ' +  str(self.id) + ', ' +self.player.name + ' ' + str(self.team_chosen)

    def setTeamChosen(self, team_id):
        # update team chosen
        self.team.chosen = True

        # fixture side variables
        self.team_chosen = True

    def setValues(self, goals_scored, goals_allowed):
        # fixture side update
        self.goals = goals_scored

        # team update
        self.team.chosen = True
        self.team.played = True
        self.team.save()

        # player update
        self.player.updatePlayer(goals_scored, goals_allowed)


class Fixture(models.Model):
    fixtureSides = models.ManyToManyField(FixtureSide)
    date = models.DateTimeField(default=dt.now)
    game_played = models.BooleanField(default=False)
    tv = models.PositiveIntegerField(default=0)

    def __str__(self):
        sides = self.fixtureSides.all()
        info = ""

        if self.game_played:
            for side in sides:
                info += side.player.name + " " + str(side.goals) + " "
            return info

        for side in sides:
            info += side.player.name + " "

        return 'id: ' +  str(self.id) + ', ' + str(self.game_played) + ": " + info

    def listPlayers(self):
        sides = self.fixtureSides.all()
        names = []
        # get the player names
        for side in sides:
            names.append(side.player.name)
        return names

    def listSideDetails(self):
        sides = self.fixtureSides.all()
        side_info = {}

        for side in sides:
            side_info[side.player.name] = {
                'team_chosen': side.team_chosen,
                'fs_id': side.id,
            }
        return side_info

    def getSide(self, player_name):
        sides = self.fixtureSides.all()
        result = None

        for side in sides:
            if side.player.name == player_name:
                result = side

        return result
