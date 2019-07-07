from django.contrib import admin
from .models import Player, Fixture, FixtureSide

# Register your models here.
admin.site.register(Player)
admin.site.register(FixtureSide)
admin.site.register(Fixture)
