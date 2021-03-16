from django.shortcuts import render,redirect
from .forms import FarmerModelForm
# Create your views here.
def listFarmers(request):
    data = {

    }
    return render(request,"Farmers/list_farmers.html",data)

def addFarmer(request):
    form = FarmerModelForm
    data = {
        'form':form
    }
    return render(request,"Farmers/add_farmer.html",data)

def editFarmer(request,pk):
    data = {

    }
    return render(request,"Farmers/edit_farmer.html",data)

def deleteFarmer(request,pk):
    data = {

    }
    return render(request,"Farmers/delete_farmer.html",data)