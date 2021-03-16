from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from system_settings.config import roles


try:
    groups = roles.INITIAL_GROUPS
    for groupobj in groups:
        group = Group.objects.filter(name=groupobj)
        if not group.exists():
            Group.objects.create(name=groupobj)
except:
    pass



# try:
#     studentgroup = Group.objects.filter(name="Student")
#
#     if not studentgroup.exists():
#         Group.objects.create(name="Student")
#
#     staffgroup = Group.objects.filter(name="Staff")
#
#     if not staffgroup.exists():
#         Group.objects.create(name="Staff")
#
#     espagroup = Group.objects.filter(name="Espa")
#
#     if not espagroup.exists():
#         Group.objects.create(name="Espa")
#
#     admingroup = Group.objects.filter(name="Administrator")
#
#     if not admingroup.exists():
#         Group.objects.create(name="Administrator")
# except:
#     pass