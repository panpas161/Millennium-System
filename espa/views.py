from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.contrib import messages
from assets.decorators.decorators import allowed_roles,staff_only
from django.contrib.auth.decorators import login_required
from assets.functions.authentication import isStaff
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import HttpResponse
from administrator.functions.auth import addUser,assignToGroup
from .filters import *
from assets.functions.pagination import getPage
from django.contrib.auth.models import User
from assets.functions.crypto import getRandomString
from unidecode import unidecode
import os

#Backend
@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def listInterestedBusinessesView(request):
    if isStaff(request):
        businessobjects = InterestedBusiness.objects.order_by("-id")
    else:
        #check if referrer is null?
        businessobjects = InterestedBusiness.objects.filter(referrer=request.user).order_by("-id")#maybe request.user is not the best thing to do
    page_get = request.GET.get("page")
    businessfilter = InterestedBusinessFilter(request.GET, queryset=businessobjects)
    businessobjects = businessfilter.qs
    # pagination
    p = Paginator(businessobjects, 5)
    try:
        page = p.page(page_get)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        return HttpResponse("Η σελίδα δεν βρέθηκε!")
    data = {
        'objects': page
    }
    return render(request,"Backend/Interested/list_interested.html",data)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def addInterestedBusinessView(request):
    form = InterestedBusinessForm
    if request.method == "POST":
        form = InterestedBusinessForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ο ενδιαφερόμενος προστέθηκε επιτυχώς!")
            return redirect("list_interested_businesses")
    data = {
        'form':form
    }
    return render(request,"Backend/Interested/add_interested.html",data)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def editInterestedBusinessView(request,pk):
    instance = InterestedBusiness.objects.get(id=pk)
    form = InterestedBusinessForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = InterestedBusinessForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Τα στοιχεία του ενδιαφερόμενου άλλαξαν επιτυχώς!")
            return redirect('list_interested_businesses')
    return render(request,"Backend/Interested/edit_interested.html",data)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def deleteInterestedBusinessView(request,pk):
    instance = InterestedBusiness.objects.get(id=pk)
    data = {
        'instance':instance
    }
    if request.method == "POST":
        instance.delete()
        messages.success(request,"Η ενδιαφερόμενη επιχείρηση διαγράφθηκε επιτυχώς!")
        return redirect('list_interested_businesses')
    return render(request,"Backend/Interested/delete_interested.html",data)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def viewInterestedBusinessView(request,pk):
    instance = InterestedBusiness.objects.get(id=pk)
    data = {
        'instance': instance
    }
    return render(request,"Backend/Interested/view_interested.html",data)

def approveInterestedBusiness(request,pk):
    instance = InterestedBusiness.objects.get(id=pk)
    username = unidecode(instance.companyname)
    addUser(
        username=username,
        password=getRandomString(15),
        email=instance.email
    )
    assignToGroup(username, "EspaUser")
    object = SubsidizedBusiness(
        firstname=instance.firstname,
        lastname=instance.lastname,
        companytype=instance.companytype,
        companyname=instance.companyname,
        location=instance.location,
        comments=instance.comments,
        phonenumber=instance.phonenumber,
        cellphone=instance.cellphone,
        email=instance.email,
        referrer=instance.referrer,
        entrydate=instance.entrydate,
        user=User.objects.get(username=username)
    )
    object.save()
    # Add services
    for service in instance.services.all():
        object.services.add(service)
    instance.delete()
    #Add mail functionality

    messages.success(request,"Η ενδιαφερόμενη επιχείρηση εγκρίθηκε με επιτυχία!")
    return redirect("list_interested_businesses")

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def listSubsidizedBusinessView(request):
    businessobjects = SubsidizedBusiness.objects.order_by("-id")
    page = getPage(request, businessobjects, SubsidizedBusinessFilter)
    data = {
        'objects':page,
        'filter':SubsidizedBusinessFilter
    }
    return render(request,"Backend/Subsidized/list_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def addSubsidizedBusinessView(request):
    form = SubsidizedBusinessForm
    data = {
        'form': form
    }
    if request.method == "POST":
        form = SubsidizedBusinessForm(request.POST)
        if form.is_valid():
            form.save()
            savedform = form.save(commit=False)
            addUser(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            assignToGroup(form.cleaned_data['username'], 'EspaUser')
            savedform.user = User.objects.get(username=form.cleaned_data['username'])
            # espausermodel = EspaUser(user=savedform.user,email=form.cleaned_data['email'])
            # espausermodel.save()
            # savedform.espauser = espausermodel
            savedform.save()
            messages.success(request, "Η επιχείρηση προστέθηκε επιτυχώς!")
            return redirect("list_subsidized_businesses")
    return render(request,"Backend/Subsidized/add_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def editSubsidizedBusinessView(request,pk):
    instance = SubsidizedBusiness.objects.get(id=pk)
    form = SubsidizedBusinessForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = SubsidizedBusinessForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Τα στοιχεία της επιχείρησης άλλαξαν επιτυχώς!")
            return redirect('list_subsidized_businesses')
    return render(request,"Backend/Subsidized/edit_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def deleteSubsidizedBusinessView(request,pk):
    instance = SubsidizedBusiness.objects.get(id=pk)
    data = {
        'instance': instance
    }
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Η επιχείρηση διαγράφθηκε επιτυχώς!")
        return redirect("list_subsidized_businesses")
    return render(request,"Backend/Subsidized/delete_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def viewSubsidizedBusinessView(request,pk):
    instance = SubsidizedBusiness.objects.get(id=pk)
    data = {
        'instance':instance
    }
    return render(request,"Backend/Subsidized/view_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def documentsSubsidizedBusinessView(request,pk):
    company = SubsidizedBusiness.objects.get(id=pk)
    documentobjects = Document.objects.filter(company=SubsidizedBusiness.objects.get(id=pk)).order_by("-id")
    page = getPage(request,documentobjects,DocumentsBackendFilter)
    data = {
        'instance': page,
        'company': company
    }
    return render(request,"Backend/Subsidized/documents_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def listServicesView(request):
    serviceobjects = EspaService.objects.order_by("-id")
    page = getPage(request, serviceobjects, ServicesFilter)
    data = {
        'objects':page
    }
    return render(request,"Backend/Services/list_services.html",data)

@login_required(login_url="login")
@staff_only
def addServiceView(request):
    form = EspaServiceForm
    data = {
        'form':form
    }
    if request.method == "POST":
        form = EspaServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Η υπηρεσία προστέθηκε επιτυχώς!")
            return redirect("list_espa_services")
    return render(request,"Backend/Services/add_service.html",data)

@login_required(login_url="login")
@staff_only
def editServiceView(request,pk):
    instance = EspaService.objects.get(id=pk)
    form = EspaServiceForm(instance=instance)
    data = {
        'instance':instance,
        'form':form
    }
    if request.method == "POST":
        form = EspaServiceForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Τα στοιχεία της υπηρεσίας άλλαξαν επιτυχώς!")
            return redirect('list_espa_services')
    return render(request,"Backend/Services/edit_service.html",data)

@login_required(login_url="login")
@staff_only
def deleteServiceView(request,pk):
    instance = EspaService.objects.get(id=pk)
    instance.delete()
    messages.success(request, "Η υπηρεσία διαγράφτηκε επιτυχώς!")
    return redirect("list_espa_services")

@login_required(login_url="login")
@staff_only
def listEspaAssociatesView(request):
    associateobjects = EspaAssociate.objects.order_by("-id")
    page = getPage(request, associateobjects, AssociatesFilter)
    data = {
        'objects':page,
        'filter':AssociatesFilter
    }
    return render(request,"Backend/Associates/list_associates.html",data)

@login_required(login_url="login")
@staff_only
def addEspaAssociateView(request):
    form = EspaAssociateForm
    data = {
        'form': form
    }
    if request.method == "POST":
        form = EspaAssociateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ο συνεργάτης προστέθηκε επιτυχώς!")
            return redirect("list_espa_associates")
    return render(request, "Backend/Associates/add_associate.html", data)

@login_required(login_url="login")
@staff_only
def editEspaAssociateView(request,pk):
    instance = EspaAssociate.objects.get(id=pk)
    form = EspaAssociateForm(instance=instance)
    data = {
        'instance': instance,
        'form': form
    }
    if request.method == "POST":
        form = EspaAssociateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Τα στοιχεία του συνεργάτη άλλαξαν επιτυχώς!")
            return redirect('list_espa_associates')
    return render(request,"Backend/Associates/edit_associates.html",data)

@login_required(login_url="login")
@staff_only
def deleteEspaAssociateView(request,pk):
    instance = EspaAssociate.objects.get(id=pk)
    instance.delete()
    messages.success(request, "Ο συνεργάτης διαγράφτηκε επιτυχώς!")
    return redirect("list_espa_associates")

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def inspectDocumentView(request,pk):
    instance = Document.objects.get(id=pk)
    if instance.inspected is False:
        instance.inspected = True
        instance.save()
        messages.success(request, "Το έγγραφο ορίστηκε ως επιθεωρημένο ειτυχώς!")
    elif instance.inspected is True:
        instance.inspected = False
        instance.save()
        messages.success(request, "Το έγγραφο ορίστηκε ως μή επιθεωρημένο ειτυχώς!")
    return redirect("documents_subsidized_businesses",instance.company.id)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def deleteDocument(request,pk):
    instance = Document.objects.get(id=pk)
    os.remove(instance.file.path)
    instance.delete()
    return redirect("documents_subsidized_businesses",instance.company.id)

@login_required(login_url="login")
@allowed_roles(roles=['Admin','Staff','Associate'])
def addDocumentView(request,pk):
    data = {

    }
    return render(request,"Backend/Subsidized/add_document.html",data)

#Frontend
@login_required(login_url="login")
@allowed_roles(roles=["EspaUser"])
def homePageView(request):
    data = {

    }
    return render(request,"Frontend/Subsidized/home_page.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["EspaUser"])
def listDocuments(request):
    objects = Document.objects.filter(company=request.user.subsidizedbusiness).order_by("-id")
    data = {
        'objects':objects,
    }
    return render(request,"Frontend/Subsidized/list_documents.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["EspaUser"])
def uploadDocuments(request):
    form = UploadDocumentForm()
    data = {
        'form':form
    }
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            savedform = form.save(commit=False)
            savedform.company = request.user.subsidizedbusiness
            savedform.inspected = False
            savedform.save()
            return redirect('espauser_list_documents')
    return render(request,"Frontend/Subsidized/upload_documents.html",data)

