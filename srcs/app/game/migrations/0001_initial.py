# Generated by Django 5.0.4 on 2024-06-15 15:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0003_user_friendrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=255)),
                ('online', models.BooleanField()),
                ('borderless', models.BooleanField()),
                ('obstacle', models.BooleanField()),
                ('square', models.BooleanField()),
                ('score', models.IntegerField(default=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('win', models.BooleanField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='game.match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='members.user')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='users',
            field=models.ManyToManyField(related_name='match', related_query_name='match', through='game.Player', to='members.user'),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online', models.BooleanField()),
                ('borderless', models.BooleanField()),
                ('obstacle', models.BooleanField()),
                ('score', models.IntegerField(default=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('matches', models.ManyToManyField(related_name='+', to='game.match')),
                ('users', models.ManyToManyField(related_name='+', to='members.user')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.user')),
            ],
        ),
    ]
