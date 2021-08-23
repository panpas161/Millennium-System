from django.shortcuts import redirect,HttpResponse
from ..functions.authentication import getUserRoles
from Millennium_System import roles

def redirectToHome(request):
    validroles = request.user.getRoles()
    if validroles is not None:
        return redirect(validroles[0]['HomePage'])
    return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")