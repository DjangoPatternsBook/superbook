from django.db import models
from django.conf import settings
from .services import SuperHeroWebAPI
import datetime


class BaseProfile(models.Model):
    USER_TYPES = (
        (0, 'Ordinary'),
        (1, 'SuperHero'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    user_type = models.IntegerField(max_length=1, null=True,
                                    choices=USER_TYPES)
    bio = models.CharField(max_length=200, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}: {:.20}". format(self.user, self.bio or "")

    @property
    def get_age(self):
        today = datetime.date.today()
        return (today.year - self.birthdate.year) - int(
            (today.month, today.day) <
            (self.birthdate.month, self.birthdate.day))

    class Meta:
        abstract = True


class SuperHeroProfile(models.Model):
    origin = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class OrdinaryProfile(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True


class Profile(SuperHeroProfile, OrdinaryProfile, BaseProfile):

    def is_superhero(self):
        return SuperHeroWebAPI.is_hero(self.user.username)
