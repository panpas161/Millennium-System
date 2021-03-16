from django.shortcuts import redirect,HttpResponse
from ..functions.authentication import getUserRoles
from system_settings.config import roles

def hasRole(request,role):
    validroles = getUserRoles(request)
    if validroles is not None:
        if role in validroles:
            return True
    return False

def redirectToHome(request):
    validroles = getUserRoles(request)
    allroles = roles.ROLES
    if validroles is not None:
        for i in range(0,len(validroles)):
            if validroles[0] == allroles[i]['Name']:
                return redirect(allroles[i]['HomePage'])
    return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")