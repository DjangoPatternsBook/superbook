from django.contrib import admin
from . import models

admin.site.register(models.Origin)
admin.site.register(models.Location)
admin.site.register(models.Sighting)
