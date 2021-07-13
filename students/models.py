from django.db import models
from Millennium_System import settings
import os
from uuid import uuid4
from cash_register.models import Receipt
from django.contrib.auth.models import User
from teachers.models import Teacher
from options.models import Prefecture,Doy

class Voucher(models.Model):
    sexoptions = (
        ("Άνδρας", "Άνδρας"), ("Γυναίκα", "Γυναίκα")
    )
    firstname = models.CharField(max_length=50,verbose_name="Όνομα")
    lastname = models.CharField(max_length=50,verbose_name="Επώνυμο")
    fathersname = models.CharField(max_length=50,verbose_name="Πατρώνυμο")
    birthdate = models.DateField(null=True,blank=True,verbose_name="Ημερ. Γεν")
    afm = models.CharField(max_length=30,verbose_name="ΑΦΜ")
    sex = models.CharField(max_length=7,choices=sexoptions,verbose_name="Φύλο")
    doy = models.ForeignKey(Doy,on_delete=models.CASCADE,verbose_name="ΔΟΥ")
    adt = models.CharField(max_length=30,verbose_name="Α.Δ.Τ./ Α.Δ")
    location = models.CharField(max_length=30,verbose_name="Πόλη")
    publishfile = models.CharField(max_length=30,verbose_name="Αρχ. Έκδοσης")
    address = models.CharField(max_length=30,verbose_name="Διεύθυνση")
    tk = models.CharField(max_length=30,verbose_name="Τ.Κ.")
    prefecture = models.ForeignKey(Prefecture,on_delete=models.CASCADE,verbose_name="Νομός")
    cellphone = models.CharField(max_length=30,verbose_name="Κινητό")
    phonenumber = models.CharField(max_length=30,verbose_name="Τηλέφωνο")
    email = models.EmailField(verbose_name="Email")
    profession = models.CharField(max_length=30,verbose_name="Επάγγελμα")
    entrydate = models.DateField(default=settings.CURRENT_DATE,verbose_name="Ημερομηνία Καταχώρησης")
    # student = models.OneToOneField("students.Student",on_delete=models.CASCADE)

class Specialty(models.Model):
    code = models.CharField(max_length=30,verbose_name="Κωδικός Τμήματος")
    specialty = models.CharField(max_length=30,verbose_name="Όνομα Ειδικότητας")
    duration = models.IntegerField(verbose_name="Διάρκεια")
    price = models.IntegerField(verbose_name="Ενδεικτική Τιμή")
    entrydate = models.DateField(null=True,default=settings.CURRENT_DATE)
    def __str__(self):
        return self.specialty

class Student(models.Model):
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            if instance.pk:
                filename = '{}.{}'.format(instance.pk, ext)
            else:
                # set filename as random string
                filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)
        return wrapper
    sexoptions = (
        ("Άνδρας","Άνδρας"),("Γυναίκα","Γυναίκα")
    )
    lastname = models.CharField(max_length=30, verbose_name="Επώνυμο")
    firstname = models.CharField(max_length=30, verbose_name="Όνομα")
    fathersname = models.CharField(max_length=30,verbose_name="πατρώνυμο")
    mothersname = models.CharField(max_length=50,null=True,verbose_name="Μητρώνυμο")
    afm = models.CharField(max_length=30,verbose_name="ΑΦΜ")
    adt = models.CharField(max_length=30,verbose_name="ΑΔΤ",)
    phonenumber = models.CharField(max_length=30,null=True,blank=True,verbose_name="Τηλέφωνο")
    cellphone = models.CharField(max_length=30,null=True,blank=True,verbose_name="Κινητό")
    email = models.EmailField(null=True,blank=True,verbose_name="Email")
    location = models.CharField(max_length=30,verbose_name="Τοποθεσία",null=True)
    price = models.IntegerField(verbose_name="Τιμή")
    discount = models.IntegerField(null=True,blank=True,verbose_name="Έκπτωση")
    voucher = models.OneToOneField(Voucher,on_delete=models.CASCADE,null=True,blank=True)
    birthdate = models.DateField(null=True,blank=True,verbose_name="Ημερομηνία Γέννησης")
    sex = models.CharField(max_length=7,choices=sexoptions,null=True,verbose_name="Φύλο")
    installments = models.IntegerField(null=True,blank=True)
    studentImage = models.ImageField(upload_to="student_images",null=True,blank=True,verbose_name="Φωτογραφία")
    entrydate = models.DateField(null=True,default=settings.CURRENT_DATE)
    specialty = models.ManyToManyField(Specialty, verbose_name="Ειδικότητα")
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.lastname + " " + self.firstname

class Department(models.Model):
    programchoices = (
        ("Απόγευμα",'Απόγευμα'),("Πρωί","Πρωί")
    )
    weekdays = (
        ("Δευτέρα","Δευτέρα"),("Τρίτη","Τρίτη"),("Τετάρτη","Τετάρτη")
    )
    departmentname = models.OneToOneField(Specialty,on_delete=models.CASCADE,verbose_name="Όνομα Τμήματος")
    teacher = models.OneToOneField("teachers.Teacher", on_delete=models.CASCADE,blank=True,null=True,verbose_name="Καθηγητής")
    program = models.CharField(choices=programchoices,max_length=50,verbose_name="Πρόγραμμα")
    start_time = models.TimeField(verbose_name="Ώρα Έναρξης")
    end_time = models.TimeField(verbose_name="Ώρα Λήξης")
    duration = models.IntegerField(verbose_name="Διάρκεια")
    remarks = models.TextField(null=True,blank=True,verbose_name="Σχόλια")
    weekday = models.CharField(max_length=30,choices=weekdays,verbose_name="Ημέρα")
    entrydate = models.DateField(null=True,default=settings.CURRENT_DATE,verbose_name="Ημερομηνία Καταχώρησης")

class Installment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    payment_number = models.IntegerField()#which installment it is e.g. first,second,third etc.
    amount = models.IntegerField()
    date = models.DateField()
    paid = models.BooleanField()
    paymentdate = models.DateField()#when will it be paid? not null nor blank
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.payment_number) + " " + str(self.student)


class Exam(models.Model):
    semesteroptions = (
        ("Α", "Α"), ("Β", "Β"), ("Γ", "Γ")
    )
    schoolyearoptions = (
        ("previous_school_year", str(settings.PREVIOUS_SCHOOL_YEAR)),
        ("current_school_year", str(settings.CURRENT_SCHOOL_YEAR))
    )
    subject = models.OneToOneField(Specialty, on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    theorygrade = models.IntegerField()
    labgrade = models.IntegerField()
    semester = models.CharField(max_length=14, choices=semesteroptions)
    schoolyear = models.CharField(max_length=20, choices=schoolyearoptions)
    remarks = models.TextField()
    entrydate = models.DateField(default=settings.CURRENT_DATE)