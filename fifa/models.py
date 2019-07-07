from django.db import models
from datetime import datetime as dt


# Create your models here.
class Player(models.Model):
    # descriptions
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=20000, default="", blank=True)

    # statistics
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_against = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def calculateGamesPlayed(self):
        return self.wins + self.draws + self.losses

    def calculateGoalDiff(self):
        return self.goals_scored + self.goals_against


class FixtureSide(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.CharField(max_length=300)
    goals = models.PositiveIntegerField(default=None, blank=True)
    
    def __str__(self):
        return self.player.name + " - " + self.team + ": " + str(self.goals)


class Fixture(models.Model):
    players = models.ManyToManyField(FixtureSide)
    data = models.DateTimeField(default=dt.now)
    game_played = models.BooleanField(default=False)

    def __str__(self):
        return str(self.game_played) + ": " + str(self.data)
