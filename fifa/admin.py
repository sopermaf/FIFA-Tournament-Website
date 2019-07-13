from django.contrib import admin
from .models import Player, Team, Fixture, FixtureSide

# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(FixtureSide)
admin.site.register(Fixture)
