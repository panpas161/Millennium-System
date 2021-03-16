from django.shortcuts import render
from .forms import loginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
from Millennium_System import settings
from assets.decorators.decorators import loggedInRedirect
# Create your views here.

@loggedInRedirect
def loginView(request):
    data = {
        'loginForm': loginForm,
    }
    if(request.method == "POST"):
        user = authenticate(request,username = request.POST['username'],password = request.POST['password'])
        if user is not None:
            login(request,user)
            messages.success(request,"Επιτυχής Σύνδεση!")
            return redirect("home")
        # else:
        #     messages.error(request,"Λάθος Στοιχεία Σύνδεσης")
        if "1=1" in request.POST['username']:
            file = open("suspicious_activity.txt","a")
            file.write("\n" + settings.CURRENT_DATE + " " + settings.CURRENT_TIME + "\nENTERIP entered possible sql injection query: " + request.POST['username'])
    return render(request,"login.html",data)

def logoutView(request):
    logout(request)
    return redirect("home")

def viewProfile(request):
    data = {

    }
    return render(request,"",data)


def generalSettingsView(request):
    data = {
    }
    return render(request,"",data)

def changePasswordView(request):
    data = {

    }
    return render(request,"",data)