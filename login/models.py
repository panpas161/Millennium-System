from django.db import models
from django.contrib.auth.models import AbstractUser
from Millennium_System import roles


class User(AbstractUser):
    picture = models.ImageField(blank=True,null=True)

    def hasModel(self, model):
        return hasattr(self, model.__name__.lower())

    def hasGroup(self, group):
        return group in self.groups.all()

    def getRoles(self):
        rolesdict = roles.ROLES
        validroles = []
        for i in range(0, len(rolesdict)):
            if self.hasGroup(rolesdict[i]['Group']) and self.hasModel(rolesdict[i]['Model']):
                validroles.append(rolesdict[i]['Name'])
            return validroles

    def hasRole(self,role):
        validroles = self.getRoles()
        if validroles is not None:
            if role in validroles:
                return True
        return False

