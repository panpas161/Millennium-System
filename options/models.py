from django.db import models

class Prefecture(models.Model):
    name = models.CharField(max_length=30)

class Municipality(models.Model):
    name = models.CharField(max_length=30)

class EducationLevel(models.Model):
    name = models.CharField(max_length=30)

class Doy(models.Model):
    name = models.CharField(max_length=30)

class FinancialSituation(models.Model):
    name = models.CharField(max_length=30)