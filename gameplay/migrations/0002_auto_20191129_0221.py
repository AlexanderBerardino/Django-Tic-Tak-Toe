# Generated by Django 2.2.7 on 2019-11-29 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='move',
            name='comment',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('first_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                   related_name='games_first_player', to=settings.AUTH_USER_MODEL)),
                ('second_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                    related_name='games_second_player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='move',
            name='game',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='gameplay.Game'),
            preserve_default=False,
        ),
    ]
