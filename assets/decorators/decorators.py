from django.http import HttpResponse
from django.shortcuts import redirect
from .functions import *
from ..functions.authentication import *
from Millennium_System import roles

#allows only specific groups to access a page
def allowed_groups(groups=[]):
    def decorator(view_func):
        def wrapper(request,*args,**kwargs):
            for i in range(0,len(groups)):
                if isInGroup(request,groups[i]):
                    return view_func(request,*args,**kwargs)
            return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")
        return wrapper
    return decorator

#allow sepcific roles to access a page
def allowed_roles(total_roles=[]):
    def decorator(view_func):
        def wrapper(request,*args,**kwargs):
            for i in range(0,len(total_roles)):
                if hasRole(request,total_roles[i]):
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

#allow only admins to access a page
def admin_only(view_func):
    def wrapper(request,*args,**kwargs):
        admin_roles = roles.ADMIN_ROLES
        for i in range(0, len(admin_roles)):
            if hasRole(request, admin_roles[i]):
                return view_func(request, *args, **kwargs)
        return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")
    return wrapper

#allow only staff and specific roles to access the page
def staff_and_roles(total_roles=[]):
    def decorator(view_func):
        def wrapper(request,*args,**kwargs):
            staff_roles = roles.STAFF_ROLES
            allow_roles = total_roles + staff_roles
            for i in range(0,len(staff_roles)):
                if hasRole(request, allow_roles):
                    return view_func(request,*args,**kwargs)
            return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")
        return wrapper
    return decorator

def homeRedirect(viewfunc):
    def wrapper(request,*args,**kwargs):
        staff_roles = roles.STAFF_ROLES
        for i in range(0,len(staff_roles)):
            if hasRole(request,staff_roles[i]):
                return viewfunc(request,*args,**kwargs)
        user = request.user
        validroles = user.getRoles()
        if validroles is not None:
            return redirect(validroles[0]['HomePage'])
        return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")
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