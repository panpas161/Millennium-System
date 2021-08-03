from django.db import models
from Millennium_System import settings
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

class Specialty(models.Model):
    name = models.CharField(max_length=30,verbose_name="Όνομα Ειδικότητας")
    code = models.CharField(max_length=30,verbose_name="Κωδικός Ειδικότητας")
    duration = models.IntegerField(verbose_name="Διάρκεια")
    price = models.IntegerField(verbose_name="Ενδεικτική Τιμή")
    entrydate = models.DateField(null=True,default=settings.CURRENT_DATE)

    def __str__(self):
        return self.name

class StudentSpecialty(models.Model):
    specialty = models.ForeignKey(Specialty,on_delete=models.CASCADE)
    student = models.ForeignKey("students.Student",on_delete=models.CASCADE,default=None,null=True)
    discount = models.IntegerField()

class Student(models.Model):
    sexoptions = (
        ("Άνδρας", "Άνδρας"),
        ("Γυναίκα", "Γυναίκα")
    )
    lastname = models.CharField(max_length=30, verbose_name="Επώνυμο")
    firstname = models.CharField(max_length=30, verbose_name="Όνομα")
    fathersname = models.CharField(max_length=30,verbose_name="πατρώνυμο")
    mothersname = models.CharField(max_length=50,null=True,verbose_name="Μητρώνυμο")
    afm = models.CharField(max_length=30,verbose_name="ΑΦΜ")
    adt = models.CharField(max_length=30,verbose_name="ΑΔΤ")
    phonenumber = models.CharField(max_length=30,null=True,blank=True,verbose_name="Τηλέφωνο")
    cellphone = models.CharField(max_length=30,null=True,blank=True,verbose_name="Κινητό")
    email = models.EmailField(null=True,blank=True,verbose_name="Email")
    location = models.CharField(max_length=30,verbose_name="Τοποθεσία")
    tk = models.CharField(max_length=30,verbose_name="Τ.Κ.")
    discount = models.IntegerField(null=True,blank=True,verbose_name="Έκπτωση")
    voucher = models.OneToOneField(Voucher,on_delete=models.CASCADE,null=True,blank=True)
    birthdate = models.DateField(null=True,blank=True,verbose_name="Ημερομηνία Γέννησης")
    sex = models.CharField(max_length=7,choices=sexoptions,null=True,verbose_name="Φύλο")
    studentimage = models.ImageField(upload_to="student_images",null=True,blank=True,verbose_name="Φωτογραφία")
    specialty = models.ManyToManyField(Specialty, verbose_name="Ειδικότητα",through="StudentSpecialty")
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    entrydate = models.DateField(default=settings.CURRENT_DATE)

    def __str__(self):
        return self.lastname + " " + self.firstname

# class Department(models.Model):
#     programchoices = (
#         ("Απόγευμα",'Απόγευμα'),("Πρωί","Πρωί")
#     )
#     weekdays = (
#         ("Δευτέρα","Δευτέρα"),("Τρίτη","Τρίτη"),("Τετάρτη","Τετάρτη")
#     )
#     departmentname = models.OneToOneField(Specialty,on_delete=models.CASCADE,verbose_name="Όνομα Τμήματος")
#     teacher = models.OneToOneField("teachers.Teacher", on_delete=models.CASCADE,blank=True,null=True,verbose_name="Καθηγητής")
#     start_time = models.TimeField(verbose_name="Ώρα Έναρξης")
#     end_time = models.TimeField(verbose_name="Ώρα Λήξης")
#     duration = models.IntegerField(verbose_name="Διάρκεια")
#     remarks = models.TextField(null=True,blank=True,verbose_name="Σχόλια")
#     weekday = models.CharField(max_length=30,choices=weekdays,verbose_name="Ημέρα")
#     entrydate = models.DateField(null=True,default=settings.CURRENT_DATE,verbose_name="Ημερομηνία Καταχώρησης")

class Department(models.Model):
    name = models.CharField(max_length=30,verbose_name="Όνομα Τμήματος")
    participants = models.ManyToManyField(Student,verbose_name="Συμμετέχοντες")
    entrydate = models.DateField(default=settings.CURRENT_DATE)

    def getParticipants(self):
        return {
            self.participants.pk: self.participants.__str__()
        }

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
    # program = models.CharField(choices=(("Απόγευμα",'Απόγευμα'),("Πρωί","Πρωί")),max_length=50,verbose_name="Πρόγραμμα")
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="studentdepartmentdays",null=True)

    def getDepartments(self):
        return {
            self.department.pk: self.department.__str__()
        }

    def __str__(self):
        return self.department.name + "-" + self.weekday

class Installment(models.Model):
    payment_number = models.IntegerField()#which installment it is e.g. first,second,third etc.
    amount = models.IntegerField()
    paid = models.BooleanField(default=False)
    paymentdate = models.DateField()#when will it be paid? not null nor blank
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,blank=True,null=True)
    entrydate = models.DateField(default=settings.CURRENT_DATE)

    # def save(self,*args,**kwargs):
    #     if self.receipt:
    #         self.paid = True
    #     else:
    #         self.paid = False

    def __str__(self):
        return str(self.payment_number) + " " + str(self.student)


class ExamGrade(models.Model):
    semesteroptions = (
        ("Α", "Α"),
        ("Β", "Β"),
        ("Γ", "Γ")
    )
    schoolyearoptions = (
        (str(settings.PREVIOUS_SCHOOL_YEAR), str(settings.PREVIOUS_SCHOOL_YEAR)),
        (str(settings.CURRENT_SCHOOL_YEAR), str(settings.CURRENT_SCHOOL_YEAR))
    )
    department = models.OneToOneField(Department,on_delete=models.CASCADE,verbose_name="Τμήμα",null=True)
    teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE,verbose_name="Καθηγητής")
    student = models.OneToOneField(Student,on_delete=models.CASCADE,verbose_name="Μαθητής")
    theorygrade = models.IntegerField(verbose_name="Βαθμός Θεωρίας")
    labgrade = models.IntegerField(verbose_name="Βαθμός Εργαστηρίου")
    semester = models.CharField(max_length=14,choices=semesteroptions,verbose_name="Εξάμηνο")
    schoolyear = models.CharField(max_length=20,choices=schoolyearoptions,verbose_name="Σχολικό Έτος")
    remarks = models.TextField(verbose_name="Σχόλια")
    entrydate = models.DateField(default=settings.CURRENT_DATE)