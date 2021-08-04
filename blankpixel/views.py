from django.shortcuts import render,redirect
from .models import *
from .forms import *
from assets.decorators.decorators import staff_only
from django.contrib.auth.decorators import login_required
from assets.functions.pagination import getPage
from .filters import *
from django.contrib import messages
from django.http import JsonResponse

@login_required(login_url="login")
@staff_only
def listClientsView(request):
    objects = Client.objects.order_by("-id")
    page = getPage(request,objects,ClientFilter)
    data = {
        'objects':page,
        'filter':ClientFilter
    }
    return render(request,"Blankpixel_Backend/Clients/list_clients.html",data)

@login_required(login_url="login")
@staff_only
def addClientView(request):
    clientform = ClientModelForm()
    servicesform = MultiServicesForm({
            "form-TOTAL_FORMS":len(Service.objects.all()),
            "form-INITIAL_FORMS":len(Service.objects.all()),
            "form-MIN_NUM_FORMS":len(Service.objects.all()),
            "form-MAX_NUM_FORMS":len(Service.objects.all())
    })
    data = {
        'form':clientform,
        'servicesform':servicesform,
        "services":Service.objects.all(),
        "services_len": len(Service.objects.all())
    }
    if request.method == "POST":
        clientform = ClientModelForm(request.POST)
        servicesform = MultiServicesForm(request.POST)
        if clientform.is_valid():
            is_client_saved = False
            savedclient = clientform.save(commit=False)
            for serviceform in servicesform:
                print(serviceform)
                if serviceform.is_valid():
                    if not is_client_saved:
                        savedclient.save()
                        is_client_saved = True
                    savedservice = serviceform.save(commit=False)
                    savedservice.client = savedclient
                    savedservice.save()
                    return redirect("list_blankpixel_clients")
    return render(request,"Blankpixel_Backend/Clients/add_client.html",data)

@login_required(login_url="login")
@staff_only
def editClientView(request,pk):
    instance = Client.objects.get(id=pk)
    form = ClientModelForm(instance=instance)
    data = {
        "form": form
    }
    return render(request,"Blankpixel_Backend/Clients/edit_client.html", data)

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

@login_required(login_url="login")
@staff_only
def getServices(request):
    services = {}
    for service in Service.objects.all():
        services.update(service.getServices())
    return JsonResponse(services)