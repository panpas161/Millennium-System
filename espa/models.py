from django.db import models
from Millennium_System import settings
from login.models import User
from django.core.validators import FileExtensionValidator

class EspaService(models.Model):
    service = models.CharField(max_length=50,verbose_name="Υπηρεσία")
    entrydate = models.DateTimeField(verbose_name="Ημερομηνία Καταχώρησης",auto_now_add=True)

    def __str__(self):
        return self.service

class EspaAssociate(models.Model):
    associatename = models.CharField(max_length=30,verbose_name="Επωνυμία Συνεργάτη")
    firstname = models.CharField(max_length=30,verbose_name="Όνομα")
    lastname = models.CharField(max_length=30,verbose_name="Επώνυμο")
    phonenumber = models.CharField(max_length=40,null=True,blank=True,verbose_name="Τηλέφωνο")
    cellphone = models.CharField(max_length=40,null=True,blank=True,verbose_name="Κινητό")
    email = models.EmailField()
    entrydate = models.DateTimeField(verbose_name="Ημερομηνία Καταχώρησης",auto_now_add=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.associatename

class InterestedBusiness(models.Model):
    firstname = models.CharField(max_length=40,verbose_name="Όνομα")
    lastname = models.CharField(max_length=40,verbose_name="Επώνυμο")
    companytype = models.CharField(max_length=40,verbose_name="Τύπος Επιχείρησης")
    companyname = models.CharField(max_length=40,verbose_name="Επωνυμία")
    location = models.CharField(max_length=40,verbose_name="Τοποθεσία")
    comments = models.TextField(null=True,blank=True,verbose_name="Σχόλια")
    phonenumber = models.CharField(max_length=40,null=True,blank=True,verbose_name="Τηλέφωνο")
    cellphone = models.CharField(max_length=40,null=True,blank=True,verbose_name="Κινητό")
    email = models.EmailField(null=True)
    services = models.ManyToManyField(EspaService,verbose_name="Υπηρεσίες",null=True,blank=False)
    referrer = models.ForeignKey(EspaAssociate,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Συστάθηκε Από")
    entrydate = models.DateTimeField(verbose_name="Ημερομηνία Καταχώρησης",auto_now_add=True)

    def __str__(self):
        return self.companyname

class SubsidizedBusiness(models.Model):
    firstname = models.CharField(max_length=40,verbose_name="Όνομα")
    lastname = models.CharField(max_length=40,verbose_name="Επώνυμο")
    companytype = models.CharField(max_length=40,verbose_name="Τύπος Επιχείρησης")
    companyname = models.CharField(max_length=40,verbose_name="Επωνυμία")
    location = models.CharField(max_length=40,verbose_name="Τοποθεσία")
    comments = models.TextField(verbose_name="Σχόλια",null=True,blank=True)
    phonenumber = models.CharField(max_length=40,verbose_name="Τηλέφωνο")
    cellphone = models.CharField(max_length=40,verbose_name="Κινητό",null=True,blank=True)
    email = models.EmailField()
    services = models.ManyToManyField(EspaService,verbose_name="Υπηρεσίες")
    referrer = models.ForeignKey(EspaAssociate,on_delete=models.CASCADE,verbose_name="Συστάθηκε Από",blank=True,null=True)
    username = models.CharField(max_length=50,null=True,blank=True)
    password = models.CharField(max_length=50,null=True,blank=True)
    entrydate = models.DateTimeField(verbose_name="Ημερομηνία Καταχώρησης",auto_now_add=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.companyname

class Document(models.Model):
    file = models.FileField(upload_to="espa_documents", verbose_name="Αρχείο", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    inspected = models.BooleanField(default=False,verbose_name="Επιθεωρήθηκε")
    comments = models.TextField(blank=True,null=True,verbose_name="Σχόλια")
    company = models.ForeignKey(SubsidizedBusiness, on_delete=models.CASCADE)
    entrydate = models.DateTimeField(auto_now_add=True)