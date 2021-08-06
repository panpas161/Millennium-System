from django.db import models
from Millennium_System import settings
from staff.models import Staff
from cash_register.models import Receipt
from django.dispatch import receiver
from django.db.models.signals import post_save

class Service(models.Model):
    name = models.CharField(max_length=30,verbose_name="Όνομα Υπηρεσίας")
    entrydate = models.DateField(default=settings.CURRENT_DATE)

    def getServices(self):
        return {
            self.pk: self.__str__()
        }
    def __str__(self):
        return self.name

class Client(models.Model):
    firstname = models.CharField(max_length=40,verbose_name="Όνομα")
    lastname = models.CharField(max_length=40,verbose_name="Επώνυμο")
    companyname = models.CharField(max_length=40,verbose_name="Επωνυμία")
    companytype = models.CharField(max_length=40,verbose_name="Τύπος Επιχείρησης")
    afm = models.CharField(max_length=30,verbose_name="ΑΦΜ")
    phonenumber = models.CharField(max_length=30,verbose_name="Τηλέφωνο")
    email = models.EmailField(null=True,blank=True)
    location = models.CharField(max_length=35,verbose_name="Τοποθεσία")
    workhours = models.FloatField(null=True,blank=True,verbose_name="Εργατοώρες")
    remarks = models.TextField(verbose_name="Παρατηρήσεις",null=True,blank=True)
    services = models.ManyToManyField(Service,verbose_name="Υπηρεσίες",through="Price")
    seller = models.ForeignKey(Staff,on_delete=models.CASCADE, null=True, blank=True, verbose_name="Πωλητής")
    entrydate = models.DateField(default=settings.CURRENT_DATE)

    def getTotalServices(self):
        return len(self.services.all())

    def getTotalCost(self):
        total_price = 0
        for price in self.price_set.all():
            total_price += price.getTotalPrice()
        return total_price

    def __str__(self):
        return self.lastname + " " + self.firstname

class Price(models.Model):  #intermediate model
    service = models.ForeignKey(Service, on_delete=models.SET_NULL,verbose_name="Υπηρεσία",null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="Τιμή")
    discount = models.FloatField(verbose_name="Έκπτωση", default=0)
    finished = models.BooleanField(default=False)

    def getTotalPrice(self):
        if self.discount:
            return float(self.price) - float(self.discount)
        else:
            return float(self.price)

    class Meta:
        unique_together = [['service', 'client']]

class Installment(models.Model):
    payment_number = models.IntegerField()#which installment it is e.g. first,second,third etc.
    amount = models.FloatField()
    paid = models.BooleanField(default=False) #it should depend if self.fields.receipt is set if it is then it's true else it's false
    paymentdate = models.DateField(null=True,blank=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,blank=True,null=True,related_name="blankpixel_client_receipt")
    entrydate = models.DateField(default=settings.CURRENT_DATE)

    def save(self,*args,**kwargs):
        if self.amount == 0:
            self.paid = True
        super().save(*args,**kwargs)

    def issueReceipt(self, recp_full_name, amount, paymentmethod, paymentway):
        Receipt(
            recipient=recp_full_name,
            client=self.client.lastname + " " + self.client.firstname,
            amount=amount,
            app=__package__,
            paymentmethod=paymentmethod,
            paymentway=paymentway
        ).save()

    def __str__(self):
        return str(self.payment_number) + " - " + str(self.client)

class OfferPDF(models.Model):
    offerfile = models.FileField(upload_to="blankpixel/offers/")
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
