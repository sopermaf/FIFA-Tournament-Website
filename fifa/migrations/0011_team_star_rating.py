# Generated by Django 2.2.2 on 2019-08-04 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0010_auto_20190804_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='star_rating',
            field=models.FloatField(default=0),
        ),
    ]
