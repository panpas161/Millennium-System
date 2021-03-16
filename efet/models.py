from django.db import models
from system_settings.efet.models import choices
# Create your models here.

class efetBusiness(models.Model):
    businesstypes = (
        ("singlebusiness","Ατομική Επιχείρηση"),("oe",'ΟΕ'),("ae","ΑΕ")
    )
    name = models.CharField(max_length=40,verbose_name="Επωνυμία επιχειρησης")
    type = models.CharField(max_length=20,verbose_name="Νομική Μορφή") #choices
    afm = models.CharField(max_length=40,verbose_name="ΑΦΜ")
    doy = models.CharField(max_length=30,verbose_name="ΔΟΥ") # choices
    branch = models.CharField(max_length=30,verbose_name="Κλάδος") #choices
    description = models.TextField(verbose_name="Περιγραφή δραστηριότητας / επαγγέλματος")
    address = models.CharField(max_length=120,verbose_name="Διεύθυνση")
    tk = models.CharField(max_length=10,verbose_name="Τ.Κ.")
    city = models.CharField(max_length=50,verbose_name="Πόλη")
    prefecture = models.CharField(max_length=50,verbose_name="Νομός") #choices?
    phonenumber = models.CharField(max_length=30,verbose_name="Τηλέφωνο")
    cellphone = models.CharField(max_length=30,verbose_name="Κινητό")
    fax = models.CharField(max_length=50,verbose_name="Fax")
    email = models.CharField(max_length=40,verbose_name="Email")
    accountant = models.CharField(max_length=40,verbose_name="Υπέυθυνος λογιστηρίου")
    contactmember = models.CharField(max_length=40,verbose_name="Υπεύθυνος επικοινωνίας")
    contactnumber = models.CharField(max_length=45,verbose_name="Τηλέφωνο υπεύθυνου επικοινωνίας")
    adt = models.CharField(max_length=35,verbose_name="Αριθμός Δελτίου Ταυτότητας / Διαβατηρίου")
    arxek = models.CharField(max_length=40,verbose_name="Αρχή έκδοσης Αριθμός Δελτίου Ταυτότητας / Διαβατηρίου")
    funding = models.BooleanField(verbose_name="Επιδότηση από ΟΑΕΔ - ΛΑΕΚ 0,45%")
    oaedmanagment = models.BooleanField(verbose_name="Ανακοίνωση προγράμματος στον ΟΑΕΔ από Millennium Education Centre")
    laekusername = models.CharField(max_length=40,verbose_name="Username ΛΑΕΚ επιχείρησης")
    laekpassword = models.CharField(max_length=40,verbose_name="Password ΛΑΕΚ επιχείρησης")

class efetStudent(models.Model):
    sexoptions = (
        ("male","Άνδρας"),("female","Γυναίκα")
    )
    doyoptions = ()
    firstname = models.CharField(max_length=40,verbose_name="Όνομα")
    lastname = models.CharField(max_length=40,verbose_name="Επώνυμο")
    fathersname = models.CharField(max_length=40,verbose_name="Πατρώνυμο")
    sex = models.CharField(max_length=40,choices=sexoptions,verbose_name="Φύλο")
    birthdate = models.DateField(verbose_name="Ημερομηνία Γέννησης")
    amka = models.CharField(max_length=40,verbose_name="ΑΜΚΑ")
    afm = models.CharField(max_length=40,verbose_name="ΑΦΜ")
    doy = models.CharField(max_length=40,choices=doyoptions,verbose_name="ΔΟΥ")
    address = models.CharField(max_length=40,verbose_name="Διεύθυνση")
    adt = models.CharField(max_length=40,verbose_name="Αριθμός Δελτίου Ταυτότητας / Διαβατηρίου")
    arxekd = models.CharField(max_length=40,verbose_name=" Αρχή έκδοσης Αριθμός Δελτίου Ταυτότητας / Διαβατηρίου")
    fax = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length=40,verbose_name="Τηλέφωνο")
    cellphone = models.CharField(max_length=40,verbose_name="Κινητό")
    email = models.EmailField(verbose_name="Email")
    remarks = models.TextField(verbose_name="Παρατηρήσεις")
    protocolnumber = models.CharField(max_length=40,verbose_name="Αριθμός Πρωτοκόλου")
    departmentnumber = models.CharField(max_length=40,verbose_name="Τμήμα")
    referenceby = models.CharField(max_length=40,verbose_name="Σύσταση από")
    business = models.ForeignKey(efetBusiness,on_delete=models.CASCADE,verbose_name="Επιχείρηση")
    oldapplication = models.BooleanField(verbose_name="Παλιά αίτηση")
