# from django.db import models
# from Millennium_System import settings
# import os
# from uuid import uuid4
# from cash_register.models import Receipt

# class Voucher(models.Model):
#     sexoptions = (
#         ("male", "Άνδρας"), ("female", "Γυναίκα")
#     )
#     doyoptions = (
#         ("test","testt"),("testtt","tt")
#     )
#     prefectureoptions = (
#         ("chalkidiki","ΧΑΛΚΙΔΙΚΗ"),("loc2","ll")
#     )
#     id = models.IntegerField(primary_key=True,verbose_name="ID")
#     firstname = models.CharField(max_length=50,verbose_name="Όνομα")
#     lastname = models.CharField(max_length=50,verbose_name="Επώνυμο")
#     fathersname = models.CharField(max_length=50,verbose_name="Πατρώνυμο")
#     birthdate = models.DateField(null=True,blank=True,verbose_name="Ημερ. Γεν")
#     afm = models.CharField(max_length=30,verbose_name="ΑΦΜ")
#     sex = models.CharField(max_length=7,choices=sexoptions,verbose_name="Φύλο")
#     doy = models.CharField(max_length=30,choices=prefectureoptions,verbose_name="ΔΟΥ")
#     adt = models.CharField(max_length=30,verbose_name="Α.Δ.Τ./ Α.Δ")
#     location = models.CharField(max_length=30,verbose_name="Πόλη")
#     publishfile = models.CharField(max_length=30,verbose_name="Αρχ. Έκδοσης")
#     address = models.CharField(max_length=30,verbose_name="Διεύθυνση")
#     tk = models.CharField(max_length=30,verbose_name="Τ.Κ.")
#     prefecture = models.CharField(max_length=30,choices=prefectureoptions,verbose_name="Νομός")
#     cellphone = models.CharField(max_length=30,verbose_name="Κινητό")
#     phonenumber = models.CharField(max_length=30,verbose_name="Τηλέφωνο")
#     email = models.EmailField(verbose_name="Email")
#     profession = models.CharField(max_length=30,verbose_name="Επάγγελμα")
#     entrydate = models.DateTimeField(auto_now_add=True,verbose_name="Ημερομηνία Καταχώρησης")
#     #student = models.ForeignKey(Student,on_delete=models.CASCADE)
#
# class Specialty(models.Model):
#     id = models.IntegerField(primary_key=True,verbose_name="ID")
#     code = models.CharField(max_length=30,verbose_name="Κωδικός Τμήματος")
#     specialty = models.CharField(max_length=30,verbose_name="Όνομα Ειδικότητας")
#     duration = models.IntegerField(verbose_name="Διάρκεια")
#     price = models.IntegerField(verbose_name="Ενδεικτική Τιμή")
#     entrydate = models.DateTimeField(null=True,auto_now_add=True)
#     def __str__(self):
#         return self.specialty
#
# class Student(models.Model):
#     def path_and_rename(path):
#         def wrapper(instance, filename):
#             ext = filename.split('.')[-1]
#             # get filename
#             if instance.pk:
#                 filename = '{}.{}'.format(instance.pk, ext)
#             else:
#                 # set filename as random string
#                 filename = '{}.{}'.format(uuid4().hex, ext)
#             # return the whole path to the file
#             return os.path.join(path, filename)
#         return wrapper
#     sexoptions = (
#         ("male","Άνδρας"),("female","Γυναίκα")
#     )
#     id = models.IntegerField(primary_key=True,verbose_name="ID")
#     lastname = models.CharField(max_length=30, verbose_name="Επώνυμο")
#     name = models.CharField(max_length=30,verbose_name="Όνομα")
#     fathersname = models.CharField(max_length=30,verbose_name="πατρώνυμο")
#     mothersname = models.CharField(max_length=50,null=True,verbose_name="Μητρώνυμο")
#     afm = models.CharField(max_length=30,verbose_name="ΑΦΜ")
#     adt = models.CharField(max_length=30,verbose_name="ΑΔΤ",)
#     phonenumber = models.CharField(max_length=30,null=True,blank=True,verbose_name="Τηλέφωνο")
#     cellphone = models.CharField(max_length=30,null=True,blank=True,verbose_name="Κινητό")
#     email = models.EmailField(null=True,blank=True,verbose_name="Email")
#     location = models.CharField(max_length=30,verbose_name="Τοποθεσία",null=True)
#     price = models.IntegerField(verbose_name="Τιμή")
#     discount = models.IntegerField(null=True,blank=True,verbose_name="Έκπτωση")
#     voucher = models.ForeignKey(Voucher,on_delete=models.CASCADE,null=True,blank=True)
#     birthdate = models.DateField(null=True,blank=True,verbose_name="Ημερομηνία Γέννησης")
#     sex = models.CharField(max_length=7,choices=sexoptions,null=True,verbose_name="Φύλο")
#     installments = models.IntegerField(null=True,blank=True)
#     studentImage = models.ImageField(null=True,blank=True,verbose_name="Φωτογραφία")
#     username = models.CharField(max_length=50,null=True,blank=True,verbose_name="Username")# not null nor blank
#     entrydate = models.DateTimeField(null=True,auto_now_add=True)
#     specialty = models.ManyToManyField(Specialty, verbose_name="Ειδικότητα")
#
#     def __str__(self):
#         return self.lastname + " " + self.name
#
# class Teacher(models.Model):
#     id = models.IntegerField(primary_key=True,verbose_name="ID")
#     firstname = models.CharField(max_length=30,verbose_name="Όνομα")
#     lastname = models.CharField(max_length=30,verbose_name="Επώνυμο")
#     phonenumber = models.CharField(max_length=30,verbose_name="Τηλέφωνο")
#     email = models.EmailField(verbose_name="Email")
#     username = models.CharField(max_length=30,verbose_name="Όνομα Χρήστη")
#     entrydate = models.DateTimeField(null=True,auto_now_add=True)
#     def __str__(self):
#         return self.lastname + " " + self.firstname
#
# class Department(models.Model):
#     programchoices = (
#         ("afternoon",'Απόγευμα'),("morning","Πρωί")
#     )
#     weekdays = (
#         ("monday","Δευτέρα"),("tuesday","Τρίτη"),("wednesday","Τετάρτη")
#     )
#     id = models.IntegerField(primary_key=True,verbose_name="ID")
#     departmentname = models.ForeignKey(Specialty,on_delete=models.CASCADE)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     program = models.CharField(choices=programchoices,max_length=50)
#     weekday = models.CharField(max_length=30,choices=weekdays,null=True)# not null
#     entrydate = models.DateTimeField(null=True,auto_now_add=True)
#
# class Installment(models.Model):
#     id = models.IntegerField(primary_key=True)
#     student = models.ForeignKey(Student,on_delete=models.CASCADE)#possible foreignkey
#     payment_number = models.IntegerField()#which installment it is e.g. first,second,third etc.
#     amount = models.IntegerField()
#     date = models.DateField()
#     paid = models.BooleanField()
#     paymentdate = models.DateField(null=True,blank=True)#when will it be paid? not null nor blank
#     receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,blank=True,null=True)#possible foreignkey
#
#     def __str__(self):
#         return str(self.payment_number) + " " + str(self.student)