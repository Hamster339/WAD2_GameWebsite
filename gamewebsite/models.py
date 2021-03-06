from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


# Represents a timezone in format "UTC+/-x"
class TimeZones(models.Model):
    timeZone = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.timeZone

# All languages available for users to speak
class Languages(models.Model):
    language = models.CharField(max_length=128)

    def __str__(self):
        return self.language


# Represents user profiles
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contactInfo = models.CharField(max_length=128)
    timeZone = models.ForeignKey(TimeZones, default=None, null=True, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Languages)

    def __str__(self):
        return self.user.username



# Represents a game
class Game(models.Model):
    name = models.CharField(max_length=128, unique=True)
    thumbNail = models.ImageField(upload_to="media/game_thumbnails", blank=True)
    description = models.CharField(max_length=128)
    date_added = models.DateField()
    slug = models.SlugField(unique=True)
    
    # needs to increment each time a user searches for a match for this game
    searches = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name

# Represents a user's request for a match on a particular game
class MatchRequests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    time = models.DateTimeField(null=True)
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return "{" \
               + self.user.username \
               + "," + self.game.name \
               + "," + self.language.language \
               + "," + self.time.__str__() \
               + "}"


# Represents two users that have been matched
class AcceptedMatches(models.Model):
    users = models.ManyToManyField(User)

    def __str__(self):
        return "{" + self.users.username + "}"
