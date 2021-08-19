from django.shortcuts import render,redirect
from .models import *
from .forms import *
from assets.decorators.decorators import staff_only
from django.contrib.auth.decorators import login_required
from assets.functions.pagination import getPage
from .filters import *
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import HttpResponse

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
    installmentsform = InstallmentForm
    data = {
        'form': clientform,
        'servicesform': servicesform,
        'services': Service.objects.all(),
        'services_len': len(Service.objects.all()),
        'installmentsform': installmentsform
    }
    if request.method == "POST":
        clientform = ClientModelForm(request.POST)
        servicesform = MultiServicesForm(request.POST)
        installmentsform = InstallmentForm(request.POST)
        if clientform.is_valid():
            is_client_saved = False
            savedclient = clientform.save(commit=False)
            for serviceform in servicesform:
                if serviceform.is_valid():
                    if not is_client_saved:
                        savedclient.save()
                        is_client_saved = True
                    savedservice = serviceform.save(commit=False)
                    savedservice.client = savedclient
                    savedservice.save()
            if installmentsform.is_valid() and is_client_saved:
                if installmentsform.cleaned_data['payment_in_advance'] != savedclient.getTotalCost() and installmentsform.cleaned_data['total_installments'] == 1:
                    return HttpResponse("<h5 style='text-align:center;'>Η προκαταβολή πρέπει να είναι ίδια με την συνολική τιμή αν η δόση ειναι 1</h5>")
                installmentsform.save(client=savedclient)
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
def viewClientServicesView(request,pk):
    instance = Client.objects.get(id=pk)
    objects = ClientService.objects.all().filter(client=instance).order_by("-id")
    # page = getPage(request,objects,None)
    data = {
        'instance':instance,
        'objects':objects,
    }
    return render(request,"Blankpixel_Backend/Clients/view_client_services.html",data)

@login_required(login_url="login")
@staff_only
def assignClientServiceView(request,pk):
    instance = Client.objects.get(id=pk)
    form = ClientServiceForm
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ClientServiceForm(request.POST)
        if form.is_valid():
            savedinstance = form.save(commit=False)
            savedinstance.client = instance
            savedinstance.save()
            messages.success(request,"Η υπηρεσία ανατέθηκε με επιτυχία στον πελάτη!")
            return redirect("view_blankpixel_client_services",instance.id)
    return render(request,"Blankpixel_Backend/Clients/assign_client_service.html",data)

@login_required(login_url="login")
@staff_only
def editAssignedClientServiceView(request,pk):
    instance = ClientService.objects.get(id=pk)
    form = ClientServiceForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ClientServiceForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect("list_blankpixel_clients",instance.client.id)
    return render(request,"Blankpixel_Backend/Clients/edit_assigned_client_service.html",data)
@login_required(login_url="login")
@staff_only
def deassignClientServiceView(request,pk):
    instance = ClientService.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Η υπηρεσία διαγράφθηκε με επιτυχία απο τον πελάτη!")
    return redirect("view_blankpixel_client_services",instance.client.id)

@login_required(login_url="login")
@staff_only
def viewClientInstallmentsView(request,pk):
    instance = Client.objects.get(id=pk)
    objects = Installment.objects.filter(client=instance).order_by("id")
    filter = InstallmentFilter
    page = getPage(request,objects,filter)
    data = {
        'objects':page,
        'instance':instance
        # 'filter':filter
    }
    return render(request,"Blankpixel_Backend/Clients/view_client_installments.html",data)

@login_required(login_url="login")
@staff_only
def payInstallmentView(request,pk):
    instance = Installment.objects.get(id=pk)
    instance.paid = True
    instance.save()
    return redirect("list_blankpixel_client_installments")

# @login_required(login_url="login")
# @staff_only
# def disapproveInstallmentView(request,pk):
#     instance = Installment.objects.get(id=pk)
#     instance.paid = False
#     instance.save()
#     return redirect("list_blankpixel_client_installments")

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
            messages.success(request, "Το τμήμα προστέθηκε με επιτυχία!")
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
def markServiceFinishedView(request,pk):
    instance = ClientService.objects.get(id=pk)
    instance.finished = True
    instance.save()
    messages.success(request,"Η υπηρεσία ορίστηκε ως ολοκληρωμένη με επιτυχία!")
    return redirect("view_blankpixel_client_services",instance.client.pk)

@login_required(login_url="login")
@staff_only
def markServiceUnfinishedView(request,pk):
    instance = ClientService.objects.get(id=pk)
    instance.finished = False
    instance.save()
    messages.success(request,"Η υπηρεσία ορίστηκε ως μη ολοκληρωμένη με επιτυχία!")
    return redirect("view_blankpixel_client_services",instance.client.pk)

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
        services.update(service.getJSONService())
    return JsonResponse(services)

@login_required(login_url="login")
@staff_only
def deletePriceView(request,pk):
    instance = ClientService.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Η υπηρεσία διαγράφτηκε με επιτυχία!")
    # return redirect("list_")