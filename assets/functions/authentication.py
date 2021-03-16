from django.contrib.auth.models import User,Group
from django.core.exceptions import ObjectDoesNotExist
from .users import getUserID
from espa.models import EspaUser
from students.models import Student
from teachers.models import Teacher
from staff.models import Staff
from administrator.models import Administrator
from django.shortcuts import HttpResponse
from enum import Enum
from system_settings.config import roles

# it'll return the user's details while searching for him in Student,Teacher,Staff and Administrator models
# def getUserDetails(request):
#     try:
#         user = Student.objects.get(user=getUserID(request.user))
#     except ObjectDoesNotExist:
#         try:
#             user = Teacher.objects.get(user=getUserID(request.user))
#         except ObjectDoesNotExist:
#             try:
#                 user = Staff.objects.get(user=getUserID(request.user))
#             except ObjectDoesNotExist:
#                 user = Administrator.objects.get(user=getUserID(request.user))
#     return user

#make it more group orienteted and delete the above
# def getUserDetails(request):
#     if request.user.groups.exists():
#         user =
#     else:
#         return None
#     return user

def isInGroup(request,group):
    return group in request.user.groups.all()

def hasUserModel(request,model):
    return hasattr(request.user,model.__name__.lower())

def getUserDetails(request):
    return hasUserModel(request)#not

def getUserRole(request):#Grabs the first valid role
    rolesdict = roles.ROLES
    for i in range(0,len(rolesdict)):
        if isInGroup(request,rolesdict[i]['Group']) and hasUserModel(request,rolesdict[i]['Model']):
            return rolesdict[i]['Name']

def getUserRoles(request):#Grabs all the available roles and returns their name NOT ID
    rolesdict = roles.ROLES
    validroles = [None] * len(rolesdict)
    hasvalidrole = False
    k = 0
    for i in range(0,len(rolesdict)):
        if isInGroup(request,rolesdict[i]['Group']) and hasUserModel(request,rolesdict[i]['Model']):
            validroles[k] = rolesdict[i]['Name']
            k += 1
    for i in range(0,len(validroles)):
        if validroles[i] is not None:
            hasvalidrole = True
            break
    if hasvalidrole:
        return validroles

def translateUserRole(role):
    translations = roles.TRANSLATED_ROLES
    return translations[role]

# def getUserRoleID(request):
#     rolesdict = roles.ROLES
#     for i in range(0,len(rolesdict)):
#         if isInGroup(request,rolesdict[i]['Group']) and hasUserModel(request,rolesdict[i]['Model']):
#             return i

# def getUserModel(request):
#     # roles = [
#     #     'admin',
#     #     'staff',
#     #     'espa',
#     #     'teacher'
#     # ]
#     for i in range(0,len(roles)):
#         if hasattr(request.user,roles[i]):
#             return getattr(request.user,roles[i]['Model'])
#     return HttpResponse("youre not in any groups")

# def getUserDetails(request):
#     model = getUserModel(request)
#     return model

#DEPRECATED FUNCTIONS


# #alternative more group-orienteted
# def getUserModel(request):
#     if isInGroup(request,"Staff"):
#         model = Staff
#     elif isInGroup(request,"Administrator"):
#         model = Administrator
#     elif isInGroup(request,"Espa"):
#         model = EspaUser
#     elif isInGroup(request,"Teacher"):
#         model = Teacher
#     else:
#         return HttpResponse("You're not in any groups!")
#     return model

# def getUserModel(request):
#     #maybe add a check if the user is in the corresponding group?
#     #if hasattr(request.user,"administrator") and isInGroup(request,"Administrator")
#     if hasattr(request.user,"administrator"):
#         model = request.user.administrator
#     elif hasattr(request.user, "staff"):
#         model = request.user.staff
#     elif hasattr(request.user, "espa"):
#         model = request.user.espa
#     elif hasattr(request.user, "teacher"):
#         model = request.user.teacher
#     else:
#         return HttpResponse("You're not in any groups!")
#     return model

#def getUserType(user):
#     if isinstance(user,Student):
#         return "Student"
#     elif isinstance(user,Teacher):
#         return "Teacher"
#     elif isinstance(user,Staff):
#         return "Staff"
#     elif isinstance(user,Administrator):
#         return "Admin"
#     elif isinstance(user,EspaUser):
#         return "EspaUser"
