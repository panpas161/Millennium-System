from django.shortcuts import render,redirect
from .models import Client
from .forms import ClientModelForm
from assets.decorators.decorators import staff_only
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
@staff_only
def listClientsView(request):
    objects = Client.objects.all()
    data = {
        'objects':objects
    }
    return render(request,"Backend/Clients/list_clients.html",data)

@login_required(login_url="login")
@staff_only
def addClientView(request):
    form = ClientModelForm()
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ClientModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"Backend/Clients/add_client.html",data)

@login_required(login_url="login")
@staff_only
def deleteClientView(request):
    data = {

    }
    return render(request,"Backend/Clients/delete_client.html",data)

@login_required(login_url="login")
@staff_only
def listDomainsView(request):
    data = {

    }
    return render(request,"Backend/Domains/list_domains.html",data)