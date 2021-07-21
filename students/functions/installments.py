from ..models import Installment,Student
from Millennium_System import settings

def validateInstallments(request):
    if request.POST.get("prokataboli") != "":
        prokataboli = int(request.POST.get("prokataboli"))
    else:
        prokataboli = 0
    if request.POST.get("discount") != "":
        discount = int(request.POST.get("discount"))
    else:
        discount = 0
    return discount,prokataboli

def studentInstallments(request):
    price = int(request.POST.get("price"))
    discount, prokataboli = validateInstallments(request)
    installment_number = int(request.POST.get("installment_number"))
    amount_per_installment = (price - prokataboli - discount) / installment_number
    idnum = request.POST.get("id")
    for i in range(0, installment_number):
        if i == 0:
            #if installment number is 1 then don't set the first installment as prokataboli
            if installment_number != 1:
                #if prokataboli is 0 set first installment as paid
                if prokataboli != 0:
                    installments = Installment(student=Student.objects.get(pk=idnum), payment_number=i + 1,amount=prokataboli,date=settings.CURRENT_DATE, paid=False)
                else:
                    installments = Installment(student=Student.objects.get(pk=idnum), payment_number=i + 1,amount=prokataboli,date=settings.CURRENT_DATE, paid=True)
            else:
                #if prokataboli is set then add 2 installments
                if prokataboli != 0:
                    installments = Installment(student=Student.objects.get(pk=idnum),
                                               payment_number=i + 1, amount=amount_per_installment, date=settings.CURRENT_DATE,
                                               paid=False)
        else:
            installments = Installment(student=Student.objects.get(pk=idnum), payment_number=i + 1,amount=amount_per_installment,date=settings.CURRENT_DATE, paid=False)
        installments.save()


def calculateInstallments(price,discount,prokataboli,installment_amount,studentobject):
    amount_per_installment = (price - discount - prokataboli) / installment_amount
    #Mark prokataboli as paid if it's zero
    if prokataboli == 0:
        Installment(
            student=studentobject,
            payment_number=0,
            amount=prokataboli,
            paid=True
        ).save()
    else:
        Installment(
            student=studentobject,
            payment_number=0,
            amount=prokataboli
        ).save()
    #Save the rest of the installments
    for i in range(1,installment_amount):
        Installment(
            student=studentobject,
            payment_number=i,
            amount=amount_per_installment
        ).save()
