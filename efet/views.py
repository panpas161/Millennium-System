from django.shortcuts import render,redirect
from .forms import EfetStudentModelForm,EfetBusinessModelForm
from assets.decorators.decorators import staff_only
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url="login")
@staff_only
def listStudents(request):
    data = {

    }
    return render(request,"efet_students/efet_list.html",data)

@login_required(login_url="login")
@staff_only
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

@login_required(login_url="login")
@staff_only
def editStudent(request,pk):
    instance = EfetStudent.objects.get(id=pk)
    form = EfetStudentModelForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = EfetStudentModelForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            redirect("list_efet_students")
    return render(request,"efet_students/efet_edit.html",data)

@login_required(login_url="login")
@staff_only
def deleteStudent(request,pk):
    data = {

    }
    return render(request,"efet_students/efet_delete.html",data)


@login_required(login_url="login")
@staff_only
def viewStudyCertificateView(request,pk):
    instance = efetStudent.objects.get(id=pk)
    data = {
        'instance':instance
    }
    return render(request,"efet_students/study_certificate.html",data)

@login_required(login_url="login")
@staff_only
def viewParticiationCertificateView(request,pk):
    instance = efetStudent.objects.get(id=pk)
    data = {
        'instance':instance
    }
    return render(request,"efet_students/participation_certificate.html",data)

@login_required(login_url="login")
@staff_only
def listBusinessesView(request):
    data = {

    }
    return render(request,"efet_businesses/list_businesses.html",data)

@login_required(login_url="login")
@staff_only
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

@login_required(login_url="login")
@staff_only
def deleteBusinessView(request,pk):
    data = {

    }
    return render(request,"efet_businesses/delete_business.html",data)

@login_required(login_url="login")
@staff_only
def editBusinessView(request,pk):
    data = {

    }
    return render(request,"efet_businesses/edit_business.html",data)
