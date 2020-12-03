from django import forms

from .models import Game, Team

class TeamSelectForm(forms.Form):
    game = forms.ModelChoiceField(queryset=Game.objects.all())
    team = forms.ModelChoiceField(queryset=Team.objects.all())
