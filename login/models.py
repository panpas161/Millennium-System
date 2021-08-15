from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .config import roles


class Role(models.Model):
    ADMIN = 0
    STAFF = 1
    STUDENT = 2
    TEACHER = 3
    ESPA_USER = 4
    ASSOCIATE = 5
    ESPA_ASSOCIATE = 6
    ROLES = (
        (ADMIN, "Administrator"),
        (STAFF, "Staff"),
        (STUDENT, "Student"),
        (TEACHER, "Teacher"),
        (ESPA_USER, "EspaUser"),
        (ASSOCIATE, "Associate"),
        (ESPA_ASSOCIATE, "EspaAssociate")
    )
    role = models.PositiveSmallIntegerField(choices=ROLES)

class User(AbstractUser):
    roles = models.ManyToManyField(Role)
    picture = models.ImageField(blank=True,null=True)

    def getRoles(self):
        return self.role

    def addRole(self,role):
        #if not self.roles.exists(roles)
        self.roles.add(role)

    def isStaff(self):
        for role in roles.STAFF_ROLES:
            if self.roles[0] == role:
                return True
        return False