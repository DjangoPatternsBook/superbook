from django.db import models
from django.conf import settings


class Origin(models.Model):
    superhero = models.ForeignKey(settings.AUTH_USER_MODEL)
    origin = models.CharField(max_length=100)

    def __str__(self):
        return "{}'s orgin: {}".format(self.superhero, self.origin)


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return "{}: ({}, {})".format(self.country,
                                     self.latitude, self.longitude)

    class Meta:
        unique_together = ("latitude", "longitude")


class Sighting(models.Model):
    superhero = models.ForeignKey(settings.AUTH_USER_MODEL)
    power = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    sighted_on = models.DateTimeField()

    def __str__(self):
        return "{}'s power {} sighted at: {} on {}".format(
            self.superhero,
            self.power,
            self.location.country,
            self.sighted_on)

    class Meta:
        unique_together = ("superhero", "power")
