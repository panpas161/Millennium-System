from django.db import models

# Create your models here.

class Client(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    brandname = models.CharField(max_length=40)
    afm = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=30)
    email = models.EmailField()
    location = models.CharField(max_length=35)
    seller = models.CharField(max_length=40)
    cost = models.IntegerField()
    entrydate = models.DateField()
