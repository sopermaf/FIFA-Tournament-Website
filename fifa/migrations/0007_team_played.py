# Generated by Django 2.2.2 on 2019-08-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0006_fixtureside_team_chosen'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='played',
            field=models.BooleanField(default=False),
        ),
    ]
