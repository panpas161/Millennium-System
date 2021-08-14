from django.shortcuts import render
from .forms import loginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
from assets.decorators.decorators import loggedInRedirect
from django.http import JsonResponse

@loggedInRedirect
def loginView(request):
    data = {
        'loginForm': loginForm,
    }
    if request.method == "POST":
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            messages.success(request,"Επιτυχής Σύνδεση!")
            return redirect("home")
        else:
            messages.error(request,"Λάθος Στοιχεία Σύνδεσης")
    return render(request,"login.html",data)

def logoutView(request):
    logout(request)
    messages.success(request,"Η αποσύνδεση ολοκληρώθηκε με επιτυχία!")
    return redirect("home")

def viewProfile(request):
    data = {

    }
    return render(request,"profile/view_profile.html",data)


def generalSettingsView(request):
    data = {
    }
    return render(request,"",data)

def changePasswordView(request):
    data = {

    }
    return render(request,"",data)

def getAccountRole(request):
    return JsonResponse({
        'role':'role'
    })