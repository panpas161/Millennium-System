from django.db import models
from Millennium_System import settings

class ReceiptType(models.Model):
    name = models.CharField(max_length=30)

class Receipt(models.Model):
    paymentmethod_choices = ('Μετρητά','Μετρητά'),('Κατάθεση στη τράπεζα','Κατάθεση στη τράπεζα'),('card','ΜΕΣΩ ΚΑΡΤΑΣ'),('check','ΕΠΙΤΑΓΗ')
    paymentway_choices = ('immediate','ΑΜΕΣΗ ΕΞΟΦΛΗΣΗ'),('oncredit','ΕΠΙ ΠΙΣΤΩΣΕΙ')
    recipient = models.CharField(max_length=25,verbose_name="Ονοματεπώνυμο εισπράκτορα")
    client = models.CharField(max_length=25,verbose_name="Πελάτης")
    reason = models.TextField(verbose_name="Αιτιολογία")
    amount = models.IntegerField(verbose_name="Ποσό")
    type = models.CharField(max_length=30,verbose_name="Τύπος Απόδειξης",default="Άλλο") #p.x espa,mathitis ktl
    paymentmethod = models.CharField(max_length=30,choices=paymentmethod_choices,verbose_name="Μέθοδος Πληρωμής")
    paymentway = models.CharField(max_length=30,choices=paymentway_choices,verbose_name="Τρόπος Πληρωμής")
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
    category_a = models.DateField(choices=categories_a,verbose_name="Κατηγορία Α")
    category_b = models.DateField(choices=categories_b,verbose_name="Κατηγορία Β")
    category_c = models.DateField(choices=categories_c,verbose_name="Κατηγορία Γ")
    paymentmethod = models.CharField(max_length=30,choices=paymentchoices,verbose_name="Μέθοδος Πληρωμής")
    type = models.CharField(max_length=30,choices=typechoices,verbose_name="Είδος")
    paymentway = models.CharField(max_length=30,choices=paymentway_choices,verbose_name="Τρόπος Πληρωμής")
    entrydate = models.DateField(default=settings.CURRENT_DATE, verbose_name="Ημερομηνία")