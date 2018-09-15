from django.db import models

# Create your models here.
class Meetup(models.Model):
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Date = models.DateField()
    Name = models.CharField(max_length=50)