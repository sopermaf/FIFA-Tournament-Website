from django.conf import settings
from django.db import models


class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    appearances = models.PositiveSmallIntegerField(default=0)
    best_overall_finish = models.PositiveSmallIntegerField(default=0)
    best_league_finish = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    favourite = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)

    points = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('points', )

    def __str__(self):
        return '{}'.format(self.user.username)
