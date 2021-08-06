from django.dispatch import receiver
from django.db.models.signals import post_init,post_save
from .models import Installment

@receiver(post_init,sender=Installment)
def updateInstallmentPaidStatus(sender,instance,**kwargs):
    if instance.receipt:
        instance.paid = True
    else:
        instance.paid = False
    instance.save()
