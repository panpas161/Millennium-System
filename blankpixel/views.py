from django.shortcuts import render,redirect
from .models import *
from .forms import *
from assets.decorators.decorators import staff_only
from django.contrib.auth.decorators import login_required
from assets.functions.pagination import getPage
from .filters import *
from django.contrib import messages

@login_required(login_url="login")
@staff_only
def listClientsView(request):
    objects = Client.objects.order_by("-id")
    page = getPage(request,objects,ClientFilter)
    data = {
        'objects':page
    }
    return render(request,"Blankpixel_Backend/Clients/list_clients.html",data)

@login_required(login_url="login")
@staff_only
def addClientView(request):
    form = ClientModelForm()
    data = {
        'form':form,
        'servicesform':MultiServicesForm,
        "objects_len":len(Service.objects.all()),
        "serviceobjects":Service.objects.all()
    }
    if request.method == "POST":
        form = ClientModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"Blankpixel_Backend/Clients/add_client.html",data)

@login_required(login_url="login")
@staff_only
def editClientView(request,pk):
    instance = Client.objects.get(id=pk)
    form = ClientModelForm(instance=instance)
    data = {
        "form": form
    }
    return render(request,"Blankpixel_Backend/Clients/add_client.html", data)

@login_required(login_url="login")
@staff_only
def deleteClientView(request,pk):
    instance = Client.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Ο πελάτης διαγράφτηκε με επιτυχία!")
    return redirect("list_blankpixel_clients")

@login_required(login_url="login")
@staff_only
def listServicesView(request):
    objects = Service.objects.order_by("-id")
    page = getPage(request,objects,ServiceFilter)
    data = {
            'objects':page
    }
    return render(request,"Blankpixel_Backend/Services/list_services.html",data)

@login_required(login_url="login")
@staff_only
def addServiceView(request):
    form = ServiceForm
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_blankpixel_services")
    return render(request,"Blankpixel_Backend/Services/add_service.html",data)

@login_required(login_url="login")
@staff_only
def editServiceView(request,pk):
    instance = Service.objects.get(id=pk)
    form = ServiceForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ServiceForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect("list_blankpixel_services")

    return render(request,"Blankpixel_Backend/Services/edit_service.html",data)

@login_required(login_url="login")
@staff_only
def deleteServiceView(request,pk):
    instance = Service.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Η υπηρεσία διαγράφτηκε με επιτυχια!")
    return redirect("list_blankpixel_clients")

@login_required(login_url="login")
@staff_only
def listDomainsView(request):
    data = {

    }
    return render(request,"Blankpixel_Backend/Domains/list_domains.html",data)