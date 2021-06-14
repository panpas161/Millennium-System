from django.db import models

class SubisidzedBusiness(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    fathersname = models.CharField(max_length=30)
    mothersname = models.CharField(max_length=30)
    phonenumber1 = models.IntegerField()
    phonenumber2 = models.IntegerField()
    email = models.EmailField()
    # municipality = models.ForeignKey()
    # diofantos_1
    # diofantos_2
    #oik_katastasi
    #ekpaideutiko epipedo
    # doy = models.ForeignKey()
    address = models.CharField(max_length=30)
    tk = models.CharField(max_length=30)
    oaed_id = models.CharField(max_length=30,verbose_name="Αριθμός Αίτησης ΟΑΕΔ")
    beneficiary_id = models.CharField(max_length=30,verbose_name="Αριθμός ID Ωφελουμένου")
    # department = models.ForeignKey()

class Document(models.Model):
    identification = models.FileField(verbose_name="Ταυτότητα")
    tax_confirmation = models.FileField(verbose_name="Βεβαίωση Εφορίας")
    id_document = models.FileField(verbose_name="ID")
    gdpr_application = models.FileField(verbose_name="Αίτηση GDPR")
    oaed_application = models.FileField(verbose_name="Αίτηση ΟΑΕΔ")