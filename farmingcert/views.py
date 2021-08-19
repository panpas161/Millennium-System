from django.shortcuts import render,redirect
from .forms import *
from assets.decorators.decorators import staff_only
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
@login_required(login_url="login")
@staff_only
def listFarmers(request):
    objects = Farmer.objects.all().order_by("-id")
    data = {
        'objects':objects
    }
    return render(request,"Farmers/list_farmers.html",data)

@login_required(login_url="login")
@staff_only
def addFarmer(request):
    form = FarmerForm
    data = {
        'form': form
    }
    if request.method == "POST":
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ο αγρότης προστέθηκε με επιτυχία!")
            return redirect("list_farmers")
    return render(request,"",data)

@login_required(login_url="login")
@staff_only
def editFarmer(request,pk):
    instance = Farmer.objects.get(id=pk)
    form = FarmerForm(instance=instance)
    data = {
        'form': form
    }
    if request.method == "POST":
        form = FarmerForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Ο αγρότης επεξεργάστηκε με επιτυχία!")
            return redirect("list_farmers")
    return render(request,"Farmers/edit_farmer.html",data)

@login_required(login_url="login")
@staff_only
def deleteFarmer(request,pk):
    instance = Farmer.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Ο αγρότης διαγράφτηκε με επιτυχία!")
    return redirect("list_farmers")

@login_required(login_url="login")
@staff_only
def listDeparments(request):
    objects = Department.objects.all().order_by("-id")
    data = {
        'objects': objects
    }
    return render(request,"Department/list_departments.html",data)

@login_required(login_url="login")
@staff_only
def addDepartment(request):
    form = DepartmentForm()
    data = {
        'form':form
    }
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Το τμήμα προστέθηκε με επιτυχία!")
            return redirect("list_farming_departments")
    return render(request,"",data)

@login_required(login_url="login")
@staff_only
def editDepartment(request,pk):
    instance = Department.objects.get(id=pk)
    form = DepartmentForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,"Το τμήμα επεξεργάστηκε με επιτυχία!")
            return redirect("list_farming_departments")
    return render(request,"Department/edit_department.html",data)

@login_required(login_url="login")
@staff_only
def deleteDepartment(request,pk):
    instance = Department.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Το τμήμα διαγράφτηκε με επιτυχία!")
    return redirect("list_departments")
