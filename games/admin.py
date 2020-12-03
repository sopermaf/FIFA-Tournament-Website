from django.contrib import admin

from .models import Game, Team


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('time', 'played', 'tv', 'modified')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars', 'player_name', 'game')

    def player_name(self, team):
        return team.player.user.username

    def game_name(self, team):
        if self.team.game:
            return str(self.team.game)
        return "---"