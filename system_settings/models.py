from django.db import models

# Create your models here.
#autofill somehow the default fields maybe a txt file defaults.txt? or in config file
class Prefecture(models.Model):
    name = models.CharField(max_length=50)

class Municipality(models.Model):
    name = models.CharField(max_length=50)

class Doy(models.Model):
    name = models.CharField(max_length=50)

