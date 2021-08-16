from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 1
    STAFF = 2
    STUDENT = 3
    TEACHER = 4
    ESPA_USER = 5
    ASSOCIATE = 6
    ESPA_ASSOCIATE = 7
    ROLES = (
        (ADMIN,"Administrator"),
        (STAFF,"Staff"),
        (STUDENT,"Student"),
        (TEACHER,"Teacher"),
        (ESPA_USER,"EspaUser"),
        (ASSOCIATE,"Associate"),
        (ESPA_ASSOCIATE,"EspaAssociate")
    )
    role = models.PositiveSmallIntegerField(choices=ROLES,null=True,blank=True)
    picture = models.ImageField(blank=True,null=True)