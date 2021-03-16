from django.db import models
from Millennium_System import settings
from cash_register.models import Receipt
#from students.models import Student,Specialty
from django.contrib.auth.models import User

class Teacher(models.Model):
    firstname = models.CharField(max_length=30,verbose_name="Όνομα")
    lastname = models.CharField(max_length=30,verbose_name="Επώνυμο")
    phonenumber = models.CharField(max_length=30,verbose_name="Τηλέφωνο")
    email = models.EmailField(blank=True,null=True,verbose_name="Email")
    entrydate = models.DateField(null=True,default=settings.CURRENT_DATE)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.lastname + " " + self.firstname

class SubjectReport(models.Model):
    subject = models.OneToOneField("students.Specialty",models.CASCADE)
    teacher = models.OneToOneField(Teacher,models.SET_NULL,null=True)
    remarks = models.TextField(null=True)#null or not?
    date = models.DateField(settings.CURRENT_DATE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    wage_per_hour = models.FloatField()
    total_hours = models.IntegerField()
    total_wage = models.FloatField(null=True)#not null

class AttendanceReport(models.Model):
    student = models.ForeignKey("students.Student",models.CASCADE)
    teacher = models.ForeignKey(Teacher, models.SET_NULL, null=True)
    date = models.DateField(settings.CURRENT_DATE)
    attendance = models.BooleanField()
    preparation = models.FloatField()
    performance = models.FloatField()
    behaviour = models.FloatField()
    cooperation = models.FloatField()
    averagegrade = models.FloatField()