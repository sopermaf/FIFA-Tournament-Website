# Generated by Django 3.1.4 on 2020-12-04 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_delete_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={},
        ),
        migrations.AddField(
            model_name='player',
            name='draws',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='goals_conceded',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='goals_scored',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='losses',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='wins',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
