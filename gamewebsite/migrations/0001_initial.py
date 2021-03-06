# Generated by Django 3.1.7 on 2021-03-26 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('thumbNail', models.ImageField(blank=True, upload_to='media/game_thumbnails')),
                ('description', models.CharField(max_length=128)),
                ('date_added', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeZones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeZone', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePicture', models.ImageField(blank=True, upload_to='media/profile_pictures')),
                ('contactInfo', models.CharField(max_length=128)),
                ('timeZone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamewebsite.timezones')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserHasLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamewebsite.acceptedlanguages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MatchRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamewebsite.game')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamewebsite.acceptedlanguages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AcceptedMatches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primaryUser', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondaryUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
