from django.db import models
from login.models import User

class Associate(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.name