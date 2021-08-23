from django.shortcuts import redirect,HttpResponse
from ..functions.authentication import getUserRoles
from Millennium_System import roles

def redirectToHome(request):
    validroles = getUserRoles(request)
    allroles = roles.ROLES
    if validroles is not None:
        for i in range(0,len(validroles)):
            if validroles[0] == allroles[i]['Name']:
                return redirect(allroles[i]['HomePage'])
    return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")