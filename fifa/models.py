from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    appearances = models.PositiveSmallIntegerField(default=0)
    best_overall_finish = models.PositiveSmallIntegerField(default=0)
    best_league_finish = models.PositiveSmallIntegerField(default=0)
    favourite = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)

    points = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    losses = models.PositiveSmallIntegerField(default=0)
    draws = models.PositiveSmallIntegerField(default=0)
    goal_difference = models.PositiveSmallIntegerField(default=0)
    goals_scored = models.PositiveSmallIntegerField(default=0)
    goals_conceded =models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('points', 'goal_difference', 'goals_scored', 'goals_conceded')

    def __str__(self):
        return self.name



class Team(models.Model):
    player = models.ForeignKey(Player, related_name='teams', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stars = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Game(models.Model):
    class TVChoices(models.TextChoices):
        MAIN = 'M'
        EXTRA = 'E'

    home_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='home_games')
    home_team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, related_name='home_games')
    home_goals = models.PositiveSmallIntegerField(default=0)
    away_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='away_games')
    away_team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, related_name='away_games')
    away_goals = models.PositiveSmallIntegerField(default=0)

    time = models.TimeField(default=timezone.now)
    played = models.BooleanField(default=False)
    tv = models.CharField(choices=TVChoices.choices, max_length=1)

    def __str__(self):
        return 'Fixture(p1="{}", p2="{}")'.format(
            self.home_player.name,
            self.away_player.name,
        )
