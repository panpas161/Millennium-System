from django.shortcuts import render,redirect

# Create your views here.
def listRoboticStudents(request):
    data = {

    }
    return render(request,"robotics_students/robotics_list.html",data)

def addRoboticStudent(request):
    data = {

    }
    return render(request,"robotics_students/robotics_add.html",data)

def editRoboticStudent(request,pk):
    data = {

    }
    return render(request,"robotics_students/robotics_edit.html",data)

def deleteRoboticStudent(request,pk):
    data = {

    }
    return render(request,"robotics_students/robotics_delete.html",data)