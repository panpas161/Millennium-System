from django.db import models
from Millennium_System import settings

class ReceiptType(models.Model):
    name = models.CharField(max_length=30)

class Receipt(models.Model):
    paymentmethod_choices = (
        ('Μετρητά', 'Μετρητά'),
        ('Κατάθεση στη τράπεζα', 'Κατάθεση στη τράπεζα'),
        ('Μέσω Κάρτας', 'Μέσω Κάρτας'),
        ('Επιταγή', 'Επιταγή')
    )
    paymentway_choices = (
        ('Άμεση Εξόφληση', 'Άμεση Εξόφληση'),
        ('Επι Πιστώσει', 'Επι Πιστώσει')
    )
    recipient = models.CharField(max_length=25,verbose_name="Ονοματεπώνυμο εισπράκτορα")
    client = models.CharField(max_length=25,verbose_name="Πελάτης")
    remarks = models.TextField(verbose_name="Παρατηρήσεις",null=True,blank=True)
    amount = models.FloatField(verbose_name="Ποσό")
    app = models.CharField(max_length=30,verbose_name="Τύπος Απόδειξης",default="Άλλο",null=True,blank=True)
    paymentmethod = models.CharField(max_length=30,choices=paymentmethod_choices,verbose_name="Μέθοδος Πληρωμής")
    paymentway = models.CharField(max_length=30,choices=paymentway_choices,verbose_name="Τρόπος Πληρωμής")
    entrydate = models.DateField(default=settings.CURRENT_DATE, verbose_name="Ημερομηνία")

    def addReceiptType(self):
        pass

class Expense(models.Model):
    categories_a = (
        ("Αμοιβές & Έξοδα Προσωπικού", "Αμοιβές & Έξοδα Προσωπικού"),
        ("Αμοιβές & Έξοδα Τρίτων", "Αμοιβές & Έξοδα Τρίτων"),
        ("Αναλώσιμα Υλικά", "Αναλώσιμα Υλικά"),
        ("Διάφορα Έξοδα", "Διάφορα Έξοδα"),
        ("Έλλειμα Ταμείου", "Έλλειμα Ταμείου"),
        ("Έπιπλα Και Λοιπός Εξοπλισμός", "Έπιπλα Και Λοιπός Εξοπλισμός"),
        ("Μηχανήματα", "Μηχανήματα"),
        ("Παροχές Τρίτων", "Παροχές Τρίτων")
    )
    categories_b = ()
    categories_c = ()
    paymentmethod_choices = (
        ('Μετρητά', 'Μετρητά'),
        ('Κατάθεση στη τράπεζα', 'Κατάθεση στη τράπεζα'),
        ('Μέσω Κάρτας', 'Μέσω Κάρτας'),
        ('Επιταγή', 'Επιταγή')
    )
    typechoices = (
        ("Απόδειξη", "Απόδειξη"),
        ("Τιμολόγιο", "Τιμολόγιο")
    )
    paymentway_choices = (
        ('Άμεση Εξόφληση', 'Άμεση Εξόφληση'),
        ('Επί Πιστώσει', 'Επί Πιστώσει')
    )
    accountable = models.CharField(max_length=30,verbose_name="Ονοματεπώνυμο Υπεύθυνου",default="Millennium IT Department")
    recipient = models.CharField(max_length=30,verbose_name="Ονοματεπώνυμο εισπράκτωρα")
    reason = models.TextField(verbose_name="Αιτιολογία")
    amount = models.FloatField(verbose_name="Ποσό")
    category_a = models.DateField(choices=categories_a,verbose_name="Κατηγορία Α")
    category_b = models.DateField(choices=categories_b,verbose_name="Κατηγορία Β")
    category_c = models.DateField(choices=categories_c,verbose_name="Κατηγορία Γ")
    paymentmethod = models.CharField(max_length=30,choices=paymentmethod_choices,verbose_name="Μέθοδος Πληρωμής")
    type = models.CharField(max_length=30,choices=typechoices,verbose_name="Είδος")
    paymentway = models.CharField(max_length=30,choices=paymentway_choices,verbose_name="Τρόπος Πληρωμής")
    entrydate = models.DateField(default=settings.CURRENT_DATE, verbose_name="Ημερομηνία")