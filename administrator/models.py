from django.db import models
from login.models import User
# Create your models here.
class Administrator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
