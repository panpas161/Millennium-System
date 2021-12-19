from django.db import models
from django.contrib.auth.models import AbstractUser
from roles.models import Role

class User(AbstractUser):
    picture = models.ImageField(blank=True,null=True)
    roles = models.ForeignKey(Role,on_delete=models.CASCADE)

    def hasModel(self, model):
        return hasattr(self, model.__name__.lower())

    def hasGroup(self, group):
        return group in self.groups.all()

    def getRoles(self):
        return self.roles.name

    def hasRole(self,role):
        validroles = self.getRoles()
        if validroles is not None:
            if role in validroles:
                return True
        return False

