from django.db import models
from Millennium_System import settings
# Create your models here.

class Receipt(models.Model):
    paymentmethod_choices = ('cash','ΜΕΤΡΗΤΑ'),('deposit','ΚΑΤΑΘΕΣΗ ΣΤΗ ΤΡΑΠΕΖΑ'),('card','ΜΕΣΩ ΚΑΡΤΑΣ'),('check','ΕΠΙΤΑΓΗ')
    paymentway_choices = ('immediate','ΑΜΕΣΗ ΕΞΟΦΛΗΣΗ'),('oncredit','ΕΠΙ ΠΙΣΤΩΣΕΙ')
    recipient = models.CharField(max_length=25, default="Millennium IT Department",verbose_name="Ονοματεπώνυμο εισπράκτορα")
    client = models.CharField(max_length=25,verbose_name="Πελάτης")
    reason = models.TextField(verbose_name="Αιτιολογία")
    amount = models.IntegerField(verbose_name="Ποσό")
    paymentmethod = models.CharField(max_length=30,choices=paymentmethod_choices,verbose_name="Μέθοδος Πληρωμής")
    paymanetway = models.CharField(max_length=30,choices=paymentway_choices,verbose_name="Τρόπος Πληρωμής")
    entrydate = models.DateField(default=settings.CURRENT_DATE, verbose_name="Ημερομηνία")

class Expense(models.Model):
    categories_a = (
        ("staffpaychecks","ΑΜΟΙΒΕΣ & ΕΞΟΔΑ ΠΡΟΣΩΠΙΚΟΥ"),("thirdpartypaychecks","ΑΜΟΙΒΕΣ & ΕΞΟΔΑ ΤΡΙΤΩΝ"),("materials","ΑΝΑΛΩΣΙΜΑ ΥΛΙΚΑ"),
        ("expenses","ΔΙΑΦΟΡΑ ΕΞΟΔΑ"),("cashshortage","ΕΛΛΕΙΜΑ ΤΑΜΕΙΟΥ"),("equipment","ΕΠΙΠΛΑ ΚΑΙ ΛΟΙΠΟΣ ΕΞΟΠΛΙΣΜΟΣ"),
        ("machinesequipment","ΜΗΧΑΝΗΜΑΤΑ"),("thirdpartyexpenses","ΠΑΡΟΧΕΣ ΤΡΙΤΩΝ")
    )
    categories_b = (
        ("test","test"),("test2","test2")
    )
    categories_c = (
        ("test","test"),("test2","test2")
    )
    paymentchoices = (
        ("cash","ΜΕΤΡΗΤΑ"),("bankdeposit","ΚΑΤΑΘΕΣΗ ΣΤΗ ΤΡΑΠΕΖΑ"),("card","ΜΕΣΩ ΚΑΡΤΑΣ"),("epay","ΗΛΕΚΤΡΟΝΙΚΗ ΠΛΗΡΩΜΗ")
    )
    typechoices = (
        ("receipt","ΑΠΟΔΕΙΞΗ"),("invoice","ΤΙΜΟΛΟΓΙΟ")
    )
    paymentway_choices = ('immediate', 'ΑΜΕΣΗ ΕΞΟΦΛΗΣΗ'), ('oncredit', 'ΕΠΙ ΠΙΣΤΩΣΕΙ')
    accountable = models.CharField(max_length=30,verbose_name="Ονοματεπώνυμο Υπεύθυνου",default="Millennium IT Department")
    recipient = models.CharField(max_length=30,verbose_name="Ονοματεπώνυμο εισπράκτωρα")
    reason = models.TextField(verbose_name="Αιτιολογία")
    amount = models.IntegerField(verbose_name="Ποσό")
    category_a = models.DateField(choices=categories_a,verbose_name="Κατηγορία Α",null=True)# not null
    category_b = models.DateField(choices=categories_b,verbose_name="Κατηγορία Β",null=True)#not null
    category_c = models.DateField(choices=categories_c,verbose_name="Κατηγορία Γ",null=True)# not null
    paymentmethod = models.CharField(max_length=30,choices=paymentchoices,verbose_name="Μέθοδος Πληρωμής")
    type = models.CharField(max_length=30,choices=typechoices,verbose_name="Είδος")
    paymentway = models.CharField(max_length=30,choices=paymentway_choices,verbose_name="Τρόπος Πληρωμής")
    entrydate = models.DateField(default=settings.CURRENT_DATE, verbose_name="Ημερομηνία")