from django.db import models

# Create your models here.


class SkiStats(models.Model):
    rank = models.IntegerField()
    athlete = models.CharField(max_length=50)
    age = models.IntegerField()
    team = models.CharField(max_length=50)
    noc = models.CharField(max_length=3)
    medal = models.CharField(max_length=10)
    t_time = models.CharField(max_length=12)

    def __str__(self):
        return self.athlete
