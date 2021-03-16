from django.shortcuts import render,redirect
from .forms import EfetStudentModelForm,EfetBusinessModelForm
# Create your views here.
def listStudents(request):
    data = {

    }
    return render(request,"efet_students/efet_list.html",data)

def addStudent(request):
    form = EfetStudentModelForm()
    data = {
        'form':form
    }
    if request.method == "POST":
        form = EfetStudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("list_efet_students")
    return render(request,"efet_students/efet_add.html",data)

def editStudent(request,pk):
    data = {

    }
    return render(request,"efet_students/efet_edit.html",data)

def deleteStudent(request,pk):
    data = {

    }
    return render(request,"efet_students/efet_delete.html",data)

def listBusinessesView(request):
    data = {

    }
    return render(request,"efet_businesses/list_businesses.html",data)

def addBusinessView(request):
    form = EfetBusinessModelForm()
    data = {
        'form':form
    }
    if request.method == "POST":
        form = EfetBusinessModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_efet_businesses")
    return render(request,"efet_businesses/add_business.html",data)

def deleteBusinessView(request,pk):
    data = {

    }
    return render(request,"efet_businesses/delete_business.html",data)

def editBusinessView(request,pk):
    data = {

    }
    return render(request,"efet_businesses/edit_business.html",data)