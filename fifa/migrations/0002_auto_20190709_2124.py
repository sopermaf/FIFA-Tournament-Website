# Generated by Django 2.2.2 on 2019-07-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fixture',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='fixture',
            old_name='players',
            new_name='fixtureSides',
        ),
        migrations.AlterField(
            model_name='player',
            name='description',
            field=models.CharField(blank=True, default='', max_length=20000),
        ),
    ]
