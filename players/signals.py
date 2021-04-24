from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from games.models import Team
from .models import Player

@receiver(pre_save, sender=Team)
def save_user_profile(sender, instance, **kwargs):
    player = Player.objects.get(pk=instance.player.pk)
    print(player)
    if instance.pk:
        print("New team")
        prev = Team.objects.get(pk=instance.pk)
        player.goals_scored -= prev.goals_scored
        player.goals_conceded -= prev.goals_conceded
        player.goal_difference -= prev.goals_scored - prev.goals_conceded

        if prev.goals_scored > prev.goals_conceded:
            player.wins -= 1
        elif prev.goals_scored == prev.goals_conceded:
            player.draws -= 1
        else:
            player.losses -= 1

    player = instance.player
    player.goals_scored += instance.goals_scored
    player.goals_conceded += instance.goals_conceded
    player.goal_difference += instance.goals_scored - instance.goals_conceded

    if instance.goals_scored > instance.goals_conceded:
        player.wins += 1
    elif instance.goals_scored == instance.goals_conceded:
        player.draws += 1
    else:
        player.losses += 1

    print(f"signal was called for f{instance.name}")

    player.save()

    print ("finished signal call")
