from django.db import models

# Create your models here.

class Notes(models.Model):
    first_third = models.CharField(max_length=255)
    second_third = models.CharField(max_length=255)
    final_third = models.CharField(max_length=255)
    overall = models.CharField(max_length=255)