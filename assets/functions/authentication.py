from system_settings.config import roles

def hasRole(request,role):
    validroles = getUserRoles(request)
    if validroles is not None:
        if role in validroles:
            return True
    return False

def isAdmin(request):
    admin_roles = roles.ADMIN_ROLES
    for i in range(0, len(admin_roles)):
        if hasRole(request, admin_roles[i]):
            return True
    return False

def isStaff(request):
    staff_roles = roles.STAFF_ROLES
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
    rolesdict = roles.ROLES
    for i in range(0,len(rolesdict)):
        if isInGroup(request,rolesdict[i]['Group']) and hasUserModel(request,rolesdict[i]['Model']):
            return rolesdict[i]['Name']

#Grabs all the available roles and returns their name NOT ID
def getUserRoles(request):
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