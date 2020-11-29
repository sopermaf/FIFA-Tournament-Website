from django.contrib import admin
from .models import Player, Team, Game


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'points', 'wins', 'draws', 'losses',
        'goal_difference', 'goals_scored', 'goals_conceded',
        'favourite',
    )
    list_filter = ('favourite', )
    search_fields = ('name', )
    ordering = ('points', 'goal_difference')
    fields = (
        'name', 'appearances', 'best_overall_finish',
        'best_league_finish', 'description'
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'player', 'stars')
    autocomplete_fields = ('player', )
    list_filter = ('player', 'stars')
    search_fields = ('name', )
    ordering = ('name', 'player__name')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    autocomplete_fields = ('home_player', 'away_player')
    list_display = (
        'time', 
        'home_team', 'home_player', 'home_goals',
        'away_goals', 'away_player', 'away_team'
    )
    list_filter = ('time', 'home_player', 'away_player')
    search_fields = ('home_player', 'away_player', 'home_team', 'away_team')
    fields = (
        'played',
        ('tv', 'time'),
        ('home_player', 'away_player'),
    )
    ordering = ('-time', )