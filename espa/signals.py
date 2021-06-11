from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import EspaAssociate

@receiver(post_delete, sender=EspaAssociate)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()