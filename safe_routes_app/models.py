from __future__ import unicode_literals

from django.db import models


class CrimeDescriptor(models.Model):
    id = models.IntegerField(primary_key=True)
    crime_key = models.CharField(max_length=100)
    crime_name = models.CharField(max_length=100)
    crime_description = models.CharField(max_length=1000)

class CrimeSeriousness(models.Model):
    id = models.IntegerField(primary_key=True)
    crime_key = models.CharField(max_length=100)
    seriousness_rate = models.IntegerField()