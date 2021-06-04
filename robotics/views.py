from django.shortcuts import render,redirect
from assets.decorators.decorators import staff_only
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
@staff_only
def listRoboticStudents(request):
    data = {

    }
    return render(request,"robotics_students/robotics_list.html",data)

@login_required(login_url="login")
@staff_only
def addRoboticStudent(request):
    data = {

    }
    return render(request,"robotics_students/robotics_add.html",data)

@login_required(login_url="login")
@staff_only
def editRoboticStudent(request,pk):
    data = {

    }
    return render(request,"robotics_students/robotics_edit.html",data)

@login_required(login_url="login")
@staff_only
def deleteRoboticStudent(request,pk):
    data = {

    }
    return render(request,"robotics_students/robotics_delete.html",data)