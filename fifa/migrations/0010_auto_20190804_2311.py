# Generated by Django 2.2.2 on 2019-08-04 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0009_auto_20190804_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='teams',
            field=models.ManyToManyField(blank=True, null=True, to='fifa.Team'),
        ),
    ]
