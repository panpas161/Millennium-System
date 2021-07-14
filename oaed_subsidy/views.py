from django.shortcuts import render,redirect
from assets.decorators.decorators import staff_only,allowed_roles
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from assets.functions.pagination import getPage
from .filters import *

@login_required(login_url="login")
@staff_only
def listSubsidizedIndividualView(request):
    objects = Department.objects.order_by("-id")
    page = getPage(request,objects,SubsidizedIndividualFilter)
    data = {
        'objects':page
    }
    return render(request,"Backend/Oaed_Subsidized_Individual/list_subsidized.html",data)

@login_required(login_url="login")
@staff_only
def addSubsidizedIndividualView(request):
    form = SubsidizedIndividualForm
    data = {
        'form':form
    }
    if request.method == "POST":
        form = SubsidizedIndividualForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Η υπηρεσία προστέθηκε επιτυχώς!")
            return redirect("list_oaed_subsidized_individuals")
    return render(request,"Backend/Oaed_Subsidized_Individual/add_subsidized.html",data)

@login_required(login_url="login")
@staff_only
def editSubsidizedIndividualView(request,pk):
    instance = SubsidizedIndividual.objects.get(id=pk)
    form = SubsidizedIndividualForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = SubsidizedIndividualForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,"Τα στοιχεία άλλαξαν επιτυχώς!")
            return redirect("list_oaed_subsidized_individuals")
    return render(request,"Backend/Oaed_Subsidized_Individual/edit_subsidized.html",data)

@login_required(login_url="login")
@staff_only
def deleteSubsidizedIndividualView(request,pk):
    instance = SubsidizedIndividual.objects.get(id=pk)
    instance.delete()
    messages.success(request, "Η απόδειξη διαγράφτηκε με επιτυχία!")
    return redirect("list_receipts")

@login_required(login_url="login")
@staff_only
def viewSubsidizedIndividualView(request,pk):
    instance = SubsidizedIndividual.objects.get(id=pk)
    data = {
        'instance':instance
    }
    return render(request,"Backend/Oaed_Subsidized_Individual/view_subsidized.html",data)

@login_required(login_url="login")
@staff_only
def listDepartmentView(request):
    objects = Department.objects.order_by("-id")
    page = getPage(request,objects,DepartmentFilter)
    data = {
        'objects':page
    }
    return render(request,"Backend/Oaed_Department/list_departments.html",data)

@login_required(login_url="login")
@staff_only
def addDepartmentView(request):
    form = DepartmentForm
    data = {
        'form':form
    }
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Το τμήμα προστέθηκε επιτυχώς!")
            return redirect("list_oaed_susidy_departments")
    return render(request,"Backend/Oaed_Department/add_department.html",data)

@login_required(login_url="login")
@staff_only
def editDepartmentView(request,pk):
    instance = Department.objects.get(id=pk)
    form = DepartmentForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = DepartmentForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,"Τα στοιχεία άλλαξαν επιτυχώς!")
            return redirect("list_oaed_susidy_departments")
    return render(request,"Backend/Oaed_Department/edit_department.html",data)

@login_required(login_url="login")
@staff_only
def deleteDepartmentView(request,pk):
    instance = Department.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Το τμήμα διαγράφθηκε επιτυχώς!")
    return redirect("list_oaed_susidy_departments")

@login_required(login_url="login")
@staff_only
def scheduleDepartmentView(request):
    data = {
        
    }
    return render(request,"Backend/Oaed_Department/schedule_department.html",data)