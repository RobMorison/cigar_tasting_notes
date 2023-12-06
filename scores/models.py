from django.db import models
from cigar.models import Cigar

# Create your models here.

class Scores(models.Model):
    wrapper = models.IntegerField()
    band = models.IntegerField()
    firmness = models.IntegerField()
    oils = models.IntegerField()
    light = models.IntegerField()
    burn = models.IntegerField()
    draw = models.IntegerField()
    consistency = models.IntegerField()
    flavor = models.IntegerField()
    smoothness = models.IntegerField()
    blend = models.IntegerField()
    progression = models.IntegerField()
    finish = models.IntegerField()
    speed = models.IntegerField()
    price = models.IntegerField()
    overall = models.IntegerField()
    cigar = models.ForeignKey(Cigar, on_delete=models.CASCADE)
