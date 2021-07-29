from django.db import models
from Millennium_System import settings
from staff.models import Staff
from cash_register.models import Receipt

class Service(models.Model):
    name = models.CharField(max_length=30)
    entrydate = models.DateField(default=settings.CURRENT_DATE)

    def __str__(self):
        return self.name

class Client(models.Model):
    firstname = models.CharField(max_length=40,verbose_name="Όνομα")
    lastname = models.CharField(max_length=40,verbose_name="Επώνυμο")
    companyname = models.CharField(max_length=40,verbose_name="Επωνυμία")
    companytype = models.CharField(max_length=40,verbose_name="Τύπος Επιχείρησης")
    afm = models.CharField(max_length=30,verbose_name="ΑΦΜ")
    phonenumber = models.CharField(max_length=30,verbose_name="Τηλέφωνο")
    email = models.EmailField()
    location = models.CharField(max_length=35,verbose_name="Τοποθεσία")
    # cost = models.IntegerField(verbose_name="Κόστος")
    workhours = models.IntegerField(null=True,blank=True,verbose_name="Εργατοώρες")
    remarks = models.TextField(verbose_name="Παρατηρήσεις",null=True,blank=True)
    services = models.ManyToManyField(Service,verbose_name="Υπηρεσίες",through="Price")
    seller = models.ForeignKey(Staff,on_delete=models.CASCADE, null=True, blank=True, verbose_name="Πωλητής")
    entrydate = models.DateField(default=settings.CURRENT_DATE)

    def __str__(self):
        return self.lastname + " " + self.firstname

class Price(models.Model):  # intermediate model
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)

class Installment(models.Model):
    payment_number = models.IntegerField()#which installment it is e.g. first,second,third etc.
    amount = models.IntegerField()
    paid = models.BooleanField(default=False) #it should depend if self.fields.receipt is set if it is then it's true else it's false
    paymentdate = models.DateField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,blank=True,null=True,related_name="blankpixel_client_installments")
    entrydate = models.DateField(default=settings.CURRENT_DATE)

    # def save(self,*args,**kwargs):
    #     if self.receipt:
    #         self.paid = True
    #     else:
    #         self.paid = False

    def __str__(self):
        return str(self.payment_number) + " " + str(self.student)