from django.db import models
from Millennium_System import settings
from cash_register.models import Receipt
#from students.models import Student,Specialty
from login.models import User

class Teacher(models.Model):
    firstname = models.CharField(max_length=30,verbose_name="Όνομα")
    lastname = models.CharField(max_length=30,verbose_name="Επώνυμο")
    phonenumber = models.CharField(max_length=30,verbose_name="Τηλέφωνο")
    email = models.EmailField(verbose_name="Email")
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    entrydate = models.DateTimeField(auto_now_add=True,verbose_name="Ημερομηνία Καταχώρησης")

    def __str__(self):
        return self.lastname + " " + self.firstname

class SubjectReport(models.Model):
    department = models.OneToOneField("students.Department",models.CASCADE,verbose_name="Τμήμα",null=True)
    teacher = models.OneToOneField(Teacher,models.SET_NULL,null=True,verbose_name="Καθηγητής")
    start_time = models.TimeField(verbose_name="Ώρα Έναρξης")
    end_time = models.TimeField(verbose_name="Ώρα Λήξης")
    material = models.TextField(null=True,blank=True,verbose_name="Διδακτέα ύλη")
    remarks = models.TextField(null=True,blank=True,verbose_name="Επιπλεόν πληροφορίες / παρατηρήσεις")
    # wage_per_hour = models.FloatField()
    # total_hours = models.IntegerField()
    # total_wage = models.FloatField()
    entrydate = models.DateTimeField(auto_now_add=True,verbose_name="Ημερομηνία Καταχώρησης")

class AttendanceReport(models.Model):
    department = models.ForeignKey("students.Department",on_delete=models.SET_NULL,null=True,verbose_name="Τμήμα")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True,verbose_name="Καθηγητής")
    preparation = models.FloatField()
    performance = models.FloatField()
    behaviour = models.FloatField()
    cooperation = models.FloatField()
    averagegrade = models.FloatField()
    attendance = models.BooleanField()
    entrydate = models.DateTimeField(auto_now_add=True,verbose_name="Ημερομηνία Καταχώρησης")
