from django.db import models

class Prefecture(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class EducationLevel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Doy(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class FinancialSituation(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name