from django.shortcuts import render
from django.http import JsonResponse
from .models import Player
import json


def index(request):
    players = Player.objects.values()
    context = {
        "page_data": json.dumps({'players': list(players)}),
    }
    return render(request, "app.html", context)
