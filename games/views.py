from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from players.models import Player
from .models import Game, Team
from .forms import TeamSelectForm


@login_required
def select_team(request):
    selected = False
    if request.method == 'POST':
        form = TeamSelectForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            team = form.cleaned_data['team']
            team.game = game
            team.save()

            selected = True
    else:
        player = get_object_or_404(Player, user=request.user)
        form = TeamSelectForm()
        form.fields['team'].queryset = Team.objects.filter(
            player=player,
            game=None
        )
        form.fields['game'].queryset = Game.objects.filter(
            players=player,
        ).exclude(
            id__in=Team.objects.exclude(game=None).values_list('game_id'),
        )

    return render(request, 'games/select_team.html', {
        'form': form,
        'selected': selected
    })
