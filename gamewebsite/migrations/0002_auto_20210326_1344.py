# Generated by Django 3.1.7 on 2021-03-26 13:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamewebsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AcceptedLanguages',
            new_name='Languages',
        ),
        migrations.RemoveField(
            model_name='acceptedmatches',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='acceptedmatches',
            name='user2',
        ),
        migrations.AddField(
            model_name='acceptedmatches',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matchrequests',
            name='capacity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='languages',
            field=models.ManyToManyField(to='gamewebsite.Languages'),
        ),
        migrations.DeleteModel(
            name='UserHasLanguage',
        ),
    ]
