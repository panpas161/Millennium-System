from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User

# @receiver(post_save,User)
# def updateUserPermissions(sender,instance,**kwargs):
#     pass
#     #add role permissions to user