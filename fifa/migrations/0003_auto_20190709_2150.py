# Generated by Django 2.2.2 on 2019-07-09 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0002_auto_20190709_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fifa.Player')),
            ],
        ),
        migrations.AlterField(
            model_name='fixtureside',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fifa.Team'),
        ),
    ]