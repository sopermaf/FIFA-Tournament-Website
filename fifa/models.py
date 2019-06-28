from django.db import models


# Create your models here.
class Player(models.Model):
    # descriptions
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=20000, default="")

    # statistics
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_against = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name + " Points: " + str(self.points) + " Goal: " + str(self.calculateGoalDiff())

    def calculateGamesPlayed(self):
        return self.wins + self.draws + self.losses

    def calculateGoalDiff(self):
        return self.goals_scored + self.goals_against