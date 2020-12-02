from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from players.models import Player


class Game(models.Model):
    class TVChoices(models.TextChoices):
        MAIN = 'main'
        EXTRA = 'extra'

    players = models.ManyToManyField(Player, related_name='games')
    time = models.TimeField(default=timezone.now)
    played = models.BooleanField(default=False)
    tv = models.CharField(choices=TVChoices.choices, max_length=10)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified', )

    def __str__(self):
        return 'Fixture({})'.format(
            ' vs '.join(player.user.username for player in self.players.all())
        )

    def clean(self):
        if self.players.count() > 2:
            raise ValidationError({
                'players': 'Only 2 players per game',
                'teams': 'Only 2 teams per game'
            })


class Team(models.Model):
    name = models.CharField(max_length=60)
    stars = models.DecimalField(max_digits=2, decimal_places=1)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='teams')
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, blank=True, null=True)
    goals_scored = models.PositiveSmallIntegerField(default=0)
    goals_conceded = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
