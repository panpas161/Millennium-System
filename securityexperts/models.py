from django.db import models

# Create your models here.

class SecurityExpert(models.Model):
    lastname = models.CharField(max_length=30)
    firstnames = models.CharField(max_length=30)
    fathersname = models.CharField(max_length=30)
    mothersname = models.CharField(max_length=30)
    birthdate = models.DateField()
    afm = models.CharField(max_length=35)
    doy = models.CharField(max_length=40)
    gender = models.CharField(max_length=30)#Choices
    adt = models.CharField(max_length=35)
    #arxekdoshs
    address = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    tk = models.CharField(max_length=10)
    prefecture = models.CharField(max_length=20)#choices
    phonenumber = models.CharField(max_length=30)
    cellphone = models.CharField(max_length=30)
    email = models.EmailField()
    educationlevel = models.CharField(max_length=30)#choices
    companyname = models.CharField(max_length=30)
    companyactivity = models.CharField(max_length=50)
    employees = models.IntegerField()#how many?
    category = models.CharField(max_length=30)#choices
    date = models.DateField()
