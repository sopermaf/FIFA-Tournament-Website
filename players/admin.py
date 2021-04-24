from django.contrib import admin
from django.utils.safestring import mark_safe

# from games.models import Team
from .models import Player


# class TeamInline(admin.TabularInline):
#     model = Team


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'points', 'wins', 'draws', 'losses',
        'goal_difference', 'goals_scored'
    )
    ordering = ('points', 'goal_difference', 'goals_scored', 'goals_conceded')
    # inlines = [TeamInline, ]

    def username(self, player):
        return player.user.username
    username.admin_order_field = 'user'

    # def teams(self, player):
    #     return mark_safe('<br>'.join(
    #         team.name for team in player.teams.all()))

    def points(self, player):
        return 0