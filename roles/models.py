from django.db import models
from django.contrib.auth.models import Group
from picklefield.fields import PickledObjectField

# class HomePage(models.Model):
#     name = models.CharField(max_length=30)
#     description = models.TextField(null=True,blank=True)
#     urlshortcut = models.CharField(max_length=30)

class Role(models.Model):
    name = models.CharField(max_length=30)
    group = models.OneToOneField(Group,on_delete=models.CASCADE)
    model = PickledObjectField()
    homepage = models.CharField(max_length=100)
    isStaff = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
