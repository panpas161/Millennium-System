#get name from 1 
from .models import Student,Specialty,Installment
def getName(id):
    objects = Student.objects.all()
    name = objects[id].name
    return name
#get array with  names
def getNames():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].name
    return array
def getLastNames():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].lastname
    return array
def getFatherNames():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].fathersname
    return array
def getAFMs():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].afm
    return array

def getADTs():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].adt
    return array

def getIDs():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].id
    return array

def getPhoneNumbers():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].phonenumber
    return array

def getCellPhones():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].cellphone
    return array

def getLocations():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].location
    return array

def getEmails():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].email
    return array

def getSpecialties():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = Specialty.objects.get(id=Student.objects.all()[i].specialty_id)
        #array[i] = objects[0].specialty.all()[0].specialty (for many to many field)
    return array

def getSpecialtiesPrices():
    objects = Student.objects.all()
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = Specialty.objects.get(id=Student.objects.all()[i].specialty_id)

def getInstallmentsIDS(studid):
    objects = Installment.objects.filter(student_id=studid)
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].id
    return array

def getInstallmentsPaymentNumber(studid):
    objects = Installment.objects.filter(student_id=studid)
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].payment_number
    return array

def getInstallmentsDate(studid):
    objects = Installment.objects.filter(student_id=studid)
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].date
    return array

def getInstallmentsAmmount(studid):
    objects = Installment.objects.filter(student_id=studid)
    array = [None] * len(objects)
    for i in range(0, len(objects)):
        array[i] = objects[i].ammount
    return array

def isInstallmentPaid(installmentid):
    objects = Installment.objects.get(id=installmentid)
    return objects.paid

def payInstallment(installmentid):
    objects = Installment.objects.get(id=installmentid)
    objects.update(paid=True)

def getInstallmentsPaidSum(studid):
    objects = Installment.objects.filter(student_id=studid,paid=True)
    sum = 0;
    for i in range(0,len(objects)):
        sum += objects[i].ammount
    return sum