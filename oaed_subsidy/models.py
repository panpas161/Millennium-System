from django.db import models
from options.models import Municipality,EducationLevel,Doy,FinancialSituation
from Millennium_System import settings
from students.models import Teacher

class DiofantosID(models.Model):
    name = models.CharField(max_length=30)
    diof_id1 = models.IntegerField()
    diof_id2 = models.IntegerField()

    def __str__(self):
        return self.name

class SubsidizedIndividual(models.Model):
    firstname = models.CharField(max_length=30,verbose_name="Όνομα")
    lastname = models.CharField(max_length=30,verbose_name="Επώνυμο")
    fathersname = models.CharField(max_length=30,verbose_name="Πατρώνυμο")
    mothersname = models.CharField(max_length=30,verbose_name="Μητρώνυμο")
    phonenumber1 = models.IntegerField(verbose_name="Τηλέφωνο 1",null=True,blank=True)
    phonenumber2 = models.IntegerField(verbose_name="Τηλέφωνο 2",null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE,verbose_name="Περιφέρεια")
    diofantos = models.ForeignKey(DiofantosID,on_delete=models.CASCADE,verbose_name="Επιλογή Διόφαντου")
    financials = models.ForeignKey(FinancialSituation,on_delete=models.CASCADE,verbose_name="Οικονομική Κατάσταση")
    education = models.ForeignKey(EducationLevel,on_delete=models.CASCADE,verbose_name="Εκπαιδευτικό Επίπεδο")
    doy = models.ForeignKey(Doy,on_delete=models.CASCADE,verbose_name="ΔΟΥ")
    address = models.CharField(max_length=30,verbose_name="Διεύθυνση")
    tk = models.CharField(max_length=30,verbose_name="Τ.Κ.")
    oaed_id = models.CharField(max_length=30,verbose_name="Αριθμός Αίτησης ΟΑΕΔ")
    beneficiary_id = models.CharField(max_length=30,verbose_name="Αριθμός ID Ωφελουμένου")
    entrydate = models.DateTimeField(auto_now_add=True,verbose_name="Ημερομηνία Καταχώρησης")

    def __str__(self):
        return self.lastname + " " + self.firstname

class Department(models.Model):
    name = models.CharField(max_length=30,verbose_name="Όνομα Τμήματος")
    participants = models.ManyToManyField(SubsidizedIndividual,verbose_name="Συμμετέχοντες")
    entrydate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DepartmentDay(models.Model):
    days = (
        ("Δευτέρα","Δευτέρα"),
        ("Τρίτη","Τρίτη"),
        ("Τετάρτη","Τετάρτη"),
        ("Πέμπτη","Πέμπτη"),
        ("Παρασκευή","Παρασκευή"),
        ("Σάββατο","Σάββατο"),
        ("Κυριακή","Κυριακή")
    )
    weekday = models.CharField(max_length=30,choices=days,verbose_name="Ημέρα")
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    start_time = models.TimeField(verbose_name="Ώρα Έναρξης")
    end_time = models.TimeField(verbose_name="Ώρα Λήξης")
    remarks = models.TextField(verbose_name="Σχόλια",null=True,blank=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name="Καθηγητής")

    # class Meta:
    #     unique_together = [["department","teacher"]]

    def __str__(self):
        return self.department.name + "-" + self.weekday

class Document(models.Model):
    identification = models.FileField(verbose_name="Ταυτότητα")
    tax_confirmation = models.FileField(verbose_name="Βεβαίωση Εφορίας")
    id_document = models.FileField(verbose_name="ID")
    gdpr_application = models.FileField(verbose_name="Αίτηση GDPR")
    oaed_application = models.FileField(verbose_name="Αίτηση ΟΑΕΔ")
    individual = models.ForeignKey(SubsidizedIndividual,on_delete=models.CASCADE)
    entrydate = models.DateTimeField(auto_now_add=True,verbose_name="Ημερομηνία Καταχώρησης")