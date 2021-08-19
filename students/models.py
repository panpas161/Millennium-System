from django.db import models
from Millennium_System import settings
from cash_register.models import Receipt
from login.models import User
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
    issuing_authority = models.CharField(max_length=30,verbose_name="Αρχ. Έκδοσης")
    address = models.CharField(max_length=30,verbose_name="Διεύθυνση")
    tk = models.CharField(max_length=30,verbose_name="Τ.Κ.")
    prefecture = models.ForeignKey(Prefecture,on_delete=models.CASCADE,verbose_name="Νομός")
    cellphone = models.CharField(max_length=30,verbose_name="Κινητό")
    phonenumber = models.CharField(max_length=30,verbose_name="Τηλέφωνο")
    email = models.EmailField(verbose_name="Email")
    profession = models.CharField(max_length=30,verbose_name="Επάγγελμα")
    entrydate = models.DateTimeField(auto_now_add=True,verbose_name="Ημερομηνία Καταχώρησης")

class Specialty(models.Model):
    name = models.CharField(max_length=30,verbose_name="Όνομα Ειδικότητας")
    code = models.CharField(max_length=30,verbose_name="Κωδικός Ειδικότητας")
    duration = models.FloatField(verbose_name="Διάρκεια")
    price = models.FloatField(verbose_name="Ενδεικτική Τιμή")
    entrydate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def getJSONSpecialty(self):
        return {
            "id":self.pk,
            "name":self.__str__(),
            "price":self.price
        }

class StudentSpecialty(models.Model):
    specialty = models.ForeignKey(Specialty,on_delete=models.CASCADE)
    student = models.ForeignKey("students.Student",on_delete=models.CASCADE,default=None,null=True)
    discount = models.FloatField(default=0,null=True,blank=True)

    def getTotalPrice(self):
        if not self.discount:
            return float(self.specialty.price)
        else:
            return float(self.specialty.price) - float(self.discount)

    class Meta:
        unique_together = [['specialty', 'student']]

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
    voucher = models.OneToOneField(Voucher,on_delete=models.CASCADE,null=True,blank=True)
    birthdate = models.DateField(null=True,blank=True,verbose_name="Ημερομηνία Γέννησης")
    sex = models.CharField(max_length=7,choices=sexoptions,null=True,verbose_name="Φύλο")
    studentimage = models.ImageField(upload_to="student_images",null=True,blank=True,verbose_name="Φωτογραφία") # maybe extend user model instead of this
    specialties = models.ManyToManyField(Specialty, verbose_name="Ειδικότητα",through="StudentSpecialty")
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    entrydate = models.DateTimeField(auto_now_add=True)

    def getTotalCost(self):
        total_price = 0
        for specialty in self.studentspecialty_set.all():
            total_price += specialty.getTotalPrice()
        return total_price

    def getCardExpirationDate(self):
        pass

    def __str__(self):
        return self.lastname + " " + self.firstname

class Department(models.Model):
    name = models.CharField(max_length=30,verbose_name="Όνομα Τμήματος")
    participants = models.ManyToManyField(Student,verbose_name="Συμμετέχοντες")
    entrydate = models.DateTimeField(auto_now_add=True)

    def getParticipants(self):
        participants = {}
        for participant in self.participants.all():
            participants.update({participant.pk: participant.__str__()})
        return participants

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
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="student_departmentdays",null=True)

    def getDepartment(self):
        return {
            self.department.pk: self.department.__str__()
        }

    def __str__(self):
        return self.department.name + "-" + self.weekday

class Installment(models.Model):
    payment_number = models.PositiveIntegerField()#which installment it is e.g. first,second,third etc.
    amount = models.FloatField()
    paid = models.BooleanField(default=False)
    paymentdate = models.DateField(null=True,blank=True)#when will it be paid? not null nor blank
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,blank=True,null=True,related_name="students_student_receipt")
    entrydate = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if self.amount == 0:
            self.paid = True
        super().save(*args,**kwargs)

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
    theorygrade = models.FloatField(verbose_name="Βαθμός Θεωρίας")
    labgrade = models.FloatField(verbose_name="Βαθμός Εργαστηρίου")
    semester = models.CharField(max_length=14,choices=semesteroptions,verbose_name="Εξάμηνο")
    schoolyear = models.CharField(max_length=20,choices=schoolyearoptions,verbose_name="Σχολικό Έτος")
    remarks = models.TextField(verbose_name="Σχόλια")
    entrydate = models.DateTimeField(auto_now_add=True)