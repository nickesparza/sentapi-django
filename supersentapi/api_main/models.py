from django.db import models

# Create your models here.

# model for individual sentai teams
class Team(models.Model):
    series_number = models.IntegerField()
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    era = models.CharField(max_length=25)
    colors = models.JSONField(default=list)
    actors = models.JSONField(default=dict)

    def __str__(self):
        return self.name
