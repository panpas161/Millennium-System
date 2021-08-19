from django.db import models

# Create your models here.

class Farmer(models.Model):
    genders = (
        ("male","Άνδρας"),("female","Γυναίκα")
    )
    regions = (
        ("halkidki","halkidikis"),("argolida","argolidas")
    )
    municipalities = (

    )
    doys = (

    )
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=35)
    fathersname = models.CharField(max_length=35)
    gender = models.CharField(max_length=20,choices=genders)
    birthdate = models.DateField()
    region = models.CharField(max_length=20,choices=regions,verbose_name="Περιφέρεια")
    municipality = models.CharField(max_length=20,choices=municipalities,verbose_name="Δήμος")
    specificregion = models.CharField(max_length=20,verbose_name="Περιοχή/Πόλη/Χωριό")
    amka = models.CharField(max_length=40)
    afm = models.CharField(max_length=40)
    doy = models.CharField(max_length=30,choices=doys,verbose_name="ΔΟΥ")
    adt = models.CharField(max_length=40)

    phonenumber = models.CharField(max_length=35)
    cellphone = models.CharField(max_length=35)
    email = models.CharField(max_length=35)
    schoolinglevel = models.CharField(max_length=35)
    book = models.BooleanField()
    price = models.IntegerField(default=25)
    notes = models.TextField()

class Department(models.Model):
    code = models.CharField(max_length=30)
    date = models.DateTimeField()
    location = models.CharField(max_length=30,default="Ν. Μουδανιά")
    room = models.TextField()
    entrydate = models.DateTimeField(auto_now_add=True)