# Generated by Django 2.2.2 on 2019-08-04 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0008_auto_20190804_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtureside',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fifa.Team'),
        ),
    ]
