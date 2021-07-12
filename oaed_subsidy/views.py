from django.shortcuts import render,redirect
from assets.decorators.decorators import staff_only,allowed_roles
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SubsidizedIndividualForm
from .models import *

@login_required(login_url="login")
@staff_only
def listSubsidizedIndividualView(request):
    data = {

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
def editSubsidizedIndividualView(request):
    data = {

    }
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