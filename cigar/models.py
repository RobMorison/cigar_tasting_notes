from django.db import models

# Create your models here.

class Cigar(models.Model):
    company = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    gauge = models.IntegerField()
    length = models.IntegerField()

