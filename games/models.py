from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from players.models import Player, Team


class Game(models.Model):
    class TVChoices(models.TextChoices):
        MAIN = 'main'
        EXTRA = 'extra'

    players = models.ManyToManyField(Player, related_name='games')
    teams = models.ManyToManyField(Team)
    time = models.TimeField(default=timezone.now)
    played = models.BooleanField(default=False)
    tv = models.CharField(choices=TVChoices.choices, max_length=10)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified')

    def __str__(self):
        return 'Fixture({})'.format(
            ' vs '.join(player.user.username for player in self.players.all())
        )

    def clean(self):
        if self.players.count() > 2 or self.players.count() > self.teams.count():
            raise ValidationError({
                'players': 'Only 2 players per game',
                'teams': 'Only 2 teams per game'
            })


