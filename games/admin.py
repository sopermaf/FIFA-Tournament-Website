from django.contrib import admin

from .models import Game, Team


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('time', 'played', 'tv', 'modified', 'playing')
    list_filter = ('played', 'tv')

    def playing(self, game):
        return ' v '.join(str(player) for player in game.players.all())


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars', 'game')

    # def player_name(self, team):
    #     return team.player.user.username

    def game_name(self, team):
        if self.team.game:
            return str(self.team.game)
        return "---"