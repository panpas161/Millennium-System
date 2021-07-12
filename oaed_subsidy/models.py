from django.db import models
from options.models import Municipality,EducationLevel,Doy,FinancialSituation

class DiofantosID(models.Model):
    name = models.CharField(max_length=30)
    diof_id1 = models.IntegerField()
    diof_id2 = models.IntegerField()

class SubsidizedIndividual(models.Model):
    firstname = models.CharField(max_length=30,verbose_name="Όνομα")
    lastname = models.CharField(max_length=30,verbose_name="Επώνυμο")
    fathersname = models.CharField(max_length=30,verbose_name="Πατρώνυμο")
    mothersname = models.CharField(max_length=30,verbose_name="Μητρώνυμο")
    phonenumber1 = models.IntegerField(verbose_name="Τηλέφωνο 1")
    phonenumber2 = models.IntegerField(verbose_name="Τηλέφωνο 2")
    email = models.EmailField()
    municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE,verbose_name="Περιφέρεια")
    diofantos = models.ForeignKey(DiofantosID,on_delete=models.CASCADE,verbose_name="Επιλογή Διόφαντου")
    financials = models.ForeignKey(FinancialSituation,on_delete=models.CASCADE,verbose_name="Οικονομική Κατάσταση")
    education = models.ForeignKey(EducationLevel,on_delete=models.CASCADE,verbose_name="Εκπαιδευτικό Επίπεδο")
    doy = models.ForeignKey(Doy,on_delete=models.CASCADE,verbose_name="ΔΟΥ")
    address = models.CharField(max_length=30,verbose_name="Διεύθυνση")
    tk = models.CharField(max_length=30,verbose_name="Τ.Κ.")
    oaed_id = models.CharField(max_length=30,verbose_name="Αριθμός Αίτησης ΟΑΕΔ")
    beneficiary_id = models.CharField(max_length=30,verbose_name="Αριθμός ID Ωφελουμένου")
    # department = models.ForeignKey()

class Document(models.Model):
    identification = models.FileField(verbose_name="Ταυτότητα")
    tax_confirmation = models.FileField(verbose_name="Βεβαίωση Εφορίας")
    id_document = models.FileField(verbose_name="ID")
    gdpr_application = models.FileField(verbose_name="Αίτηση GDPR")
    oaed_application = models.FileField(verbose_name="Αίτηση ΟΑΕΔ")