from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Player, Team


class TeamInline(admin.TabularInline):
    model = Team


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('username', 'points', 'teams')
    ordering = ('points', )
    inlines = [TeamInline, ]

    def username(self, player):
        return player.user.username
    username.admin_order_field = 'user'

    def teams(self, player):
        return mark_safe('<br>'.join(
            team.name for team in player.teams.all()))
