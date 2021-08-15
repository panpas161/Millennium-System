from django.db import models
from login.models import User
# Create your models here.

class Staff(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(null=True,blank=True)
    phonenumber = models.CharField(max_length=30,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,verbose_name="Φωτογραφία")
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.lastname + " " + self.firstname