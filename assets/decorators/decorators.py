from django.http import HttpResponse
from django.shortcuts import redirect
from .functions import *
from ..functions.authentication import *
from system_settings.config import roles

#allows only specific groups to access a page
def allowed_groups(roles=[]):
    def decorator(view_func):
        def wrapper(request,*args,**kwargs):
            for i in range(0,len(roles)):
                if isInGroup(request,roles[i]):
                    return view_func(request,*args,**kwargs)
            return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")
        return wrapper
    return decorator

def allowed_roles(roles=[]):
    def decorator(view_func):
        def wrapper(request,*args,**kwargs):
            for i in range(0,len(roles)):
                if hasRole(request,roles[i]):
                    return view_func(request,*args,**kwargs)
            return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")
        return wrapper
    return decorator

#allow only staff to access a page
def staff_only(view_func):
    def wrapper(request,*args,**kwargs):
        staff_roles = roles.STAFF_ROLES
        for i in range(0, len(staff_roles)):
            if hasRole(request, staff_roles[i]):
                return view_func(request, *args, **kwargs)
        return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")
    return wrapper

def homeRedirect(viewfunc):
    def wrapper(request,*args,**kwargs):
        staff_roles = roles.STAFF_ROLES
        for i in range(0,len(staff_roles)):
            if hasRole(request,staff_roles[i]):
                return viewfunc(request,*args,**kwargs)
        return redirectToHome(request)
    return wrapper

#if user is logged in redirect him to his group's home page
def loggedInRedirect(viewfunc):
    def wrapper(request,*args,**kwargs):
        if str(request.user) != "AnonymousUser":
            if request.user.groups.exists():#fix this with roles not groups
                return redirectToHome(request.user.groups.all()[0].name)
            else:
                return HttpResponse("Δεν είστε μέλος κάποιας ομάδας παρακαλώ επικοινωνήστε με τον διαχειριστή του συστήματος")
        else:
            return viewfunc(request,*args,**kwargs)
    return wrapper