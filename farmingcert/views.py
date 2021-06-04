from django.shortcuts import render,redirect
from .forms import FarmerModelForm
from assets.decorators.decorators import staff_only
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
@staff_only
def listFarmers(request):
    data = {

    }
    return render(request,"Farmers/list_farmers.html",data)

@login_required(login_url="login")
@staff_only
def addFarmer(request):
    form = FarmerModelForm
    data = {
        'form':form
    }
    return render(request,"Farmers/add_farmer.html",data)

@login_required(login_url="login")
@staff_only
def editFarmer(request,pk):
    data = {

    }
    return render(request,"Farmers/edit_farmer.html",data)

@login_required(login_url="login")
@staff_only
def deleteFarmer(request,pk):
    data = {

    }
    return render(request,"Farmers/delete_farmer.html",data)