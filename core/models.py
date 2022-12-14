from django.db import models

# Create your models here.
class Fixture(models.Model):
    team1 = models.CharField(max_length=128)
    team2 = models.CharField(max_length=128)
    team1_goals = models.IntegerField()
    team2_goals = models.IntegerField()