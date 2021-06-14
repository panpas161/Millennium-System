from system_settings.config.roles import ROLES,STAFF_ROLES,ADMIN_ROLES,TRANSLATED_ROLES
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def hasRole(request,role):
    validroles = getUserRoles(request)
    if validroles is not None:
        if role in validroles:
            return True
    return False

def isAdmin(request):
    admin_roles = ADMIN_ROLES
    for i in range(0, len(admin_roles)):
        if hasRole(request, admin_roles[i]):
            return True
    return False

def isStaff(request):
    staff_roles = STAFF_ROLES
    for i in range(0, len(staff_roles)):
        if hasRole(request, staff_roles[i]):
            return True
    return False

def isInGroup(request,group):
    return group in request.user.groups.all()

def hasUserModel(request,model):
    return hasattr(request.user,model.__name__.lower())

def getUserDetails(request):
    return hasUserModel(request)#not

#Grabs the first valid role
def getUserRole(request):
    rolesdict = ROLES
    for i in range(0,len(rolesdict)):
        if isInGroup(request,rolesdict[i]['Group']) and hasUserModel(request,rolesdict[i]['Model']):
            return rolesdict[i]['Name']

#Grabs all the available roles and returns their name NOT ID
def getUserRoles(request):
    rolesdict = ROLES
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
    translations = TRANSLATED_ROLES
    return translations[role]

def createGroup(groupname): #add permissions for more security
    group = Group.objects.filter(name=groupname)
    if not group.exists():
        Group.objects.create(name=groupname)

def assignToGroup(username,groupname):
    createGroup(groupname)
    group = Group.objects.get(name=groupname)
    user = User.objects.get(username=username)
    user.groups.add(group)

#create user and add him to his role's group
def addUser(username,email,password,role):
    allroles = ROLES
    user = User.objects.create_user(username=username,email=email,password=password)
    user.save()
    for i in range(0,len(allroles)):
        if allroles[i]['Name'] == role:
            group = allroles[i]['Group']
            break
    assignToGroup(username,group)

def changeUserPassword(username,password):
    object = User.objects.get(username=username)
    object.set_password(password)
    object.save()

