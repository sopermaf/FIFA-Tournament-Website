from django.db import models
from datetime import datetime as dt


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    chosen = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ": " + str(self.chosen)


class Player(models.Model):
    # descriptions
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=20000, default="", blank=True)
    teams = models.ManyToManyField(Team)

    # statistics
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_against = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def allTeams(self):
       return self.teams.all()

    def unusedTeams(self):
        return self.teams.all().filter(chosen=False)

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
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    goals = models.PositiveIntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.player.name

    def updateTeam(self):
        self.team.chosen = True

    @classmethod
    def createSide(cls, player, team):
        team.chosen = True
        return cls(player=player, team=team, goals=0)


class Fixture(models.Model):
    fixtureSides = models.ManyToManyField(FixtureSide)
    date = models.DateTimeField(default=dt.now)
    game_played = models.BooleanField(default=False)

    def __str__(self):
        sides = self.fixtureSides.all()
        info = ""

        if self.game_played:
            for side in sides:
                info += side.player.name + " " + str(side.goals) + " "
            return info

        for side in sides:
            info += side.player.name + " "

        return str(self.game_played) + ": " + info

    def listPlayers(self):
        sides = self.fixtureSides.all()
        names = []
        # get the player names
        for side in sides:
            names.append(side.player.name)
        return names
