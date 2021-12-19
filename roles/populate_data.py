from Millennium_System.roles import ROLES
from django.contrib.auth.models import Group
from .models import Role

def createRoles(apps, schema_editor):
    for role in ROLES:
        Role(
            name=role['Name'],
            group=Group.objects.get_or_create(name=role['Group']),
            model=role['Model'],
            homepage=role['HomePage'],
            isStaff=role['isStaff'],
            isAdmin=role['isAdmin']
        ).save()