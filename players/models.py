from typing import DefaultDict
from django.conf import settings
from django.db import models
from django.db.models import Sum, Count, Q, F


class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    appearances = models.PositiveSmallIntegerField(default=0)
    best_overall_finish = models.PositiveSmallIntegerField(default=0)
    best_league_finish = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    favourite = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)

    points = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    draws = models.PositiveSmallIntegerField(default=0)
    losses = models.PositiveSmallIntegerField(default=0)
    goal_difference = models.PositiveSmallIntegerField(default=0)
    goals_scored = models.PositiveSmallIntegerField(default=0)
    goals_conceded = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return '{}'.format(self.user.username)
