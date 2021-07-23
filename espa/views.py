from django.shortcuts import render
from assets.functions.mailer import sendEspaCredentials
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.contrib import messages
from assets.decorators.decorators import allowed_roles,staff_only,admin_only
from django.contrib.auth.decorators import login_required
from assets.functions.authentication import isStaff,hasRole,isAdmin
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import HttpResponse
from assets.functions.authentication import addUser
from .filters import *
from assets.functions.pagination import getPage
from django.contrib.auth.models import User
from assets.functions.crypto import getRandomString
from unidecode import unidecode
import os
from django.views.generic.edit import FormView
from .handlers import uploadEspaDocumentFiles

#Backend
@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def listInterestedBusinessesView(request):
    if isStaff(request) or hasRole(request,"Associate"):
        businessobjects = InterestedBusiness.objects.order_by("-id")
    else:
        businessobjects = InterestedBusiness.objects.filter(referrer=request.user.espaassociate).order_by("-id")
    page = getPage(request,businessobjects,InterestedBusinessFilter)
    data = {
        'objects': page,
        'filter':InterestedBusinessFilter
    }
    return render(request,"Espa_Backend/Interested/list_interested.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def addInterestedBusinessView(request):
    form = InterestedBusinessForm
    if request.method == "POST":
        form = InterestedBusinessForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ο ενδιαφερόμενος προστέθηκε επιτυχώς!")
            return redirect("list_espa_interested_businesses")
    data = {
        'form':form
    }
    return render(request,"Espa_Backend/Interested/add_interested.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def editInterestedBusinessView(request,pk):
    instance = InterestedBusiness.objects.get(id=pk)
    if instance.referrer:
        if instance.referrer.user == request.user:
            form = InterestedBusinessForm(instance=instance)
    else:
        return HttpResponse("<h2 style='text-align:center;'>Δεν επιτρέπεται η πρόσβαση</h2>")
    data = {
        'form':form
    }
    # if not isStaff(request):
    #     form.pop("referrer")
    if request.method == "POST":
        form = InterestedBusinessForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Τα στοιχεία του ενδιαφερόμενου άλλαξαν επιτυχώς!")
            return redirect('list_espa_interested_businesses')
    return render(request,"Espa_Backend/Interested/edit_interested.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def deleteInterestedBusinessView(request,pk):
    instance = InterestedBusiness.objects.get(id=pk)
    data = {
        'instance':instance
    }
    if request.method == "POST":
        instance.delete()
        messages.success(request,"Η ενδιαφερόμενη επιχείρηση διαγράφθηκε επιτυχώς!")
        return redirect('list_espa_interested_businesses')
    return render(request,"Espa_Backend/Interested/delete_interested.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def viewInterestedBusinessView(request,pk):
    instance = InterestedBusiness.objects.get(id=pk)
    data = {
        'instance': instance
    }
    return render(request,"Espa_Backend/Interested/view_interested.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def approveInterestedBusiness(request,pk):
    instance = InterestedBusiness.objects.get(id=pk)
    username = unidecode(instance.companyname)
    password = getRandomString(15)
    role = "EspaUser"
    addUser(
        username=username,
        password=password,
        email=instance.email,
        role=role
    )
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
    #Send mail with credentials
    sendEspaCredentials(
        username=username,
        password=password,
        email=instance.email,
        role=role
    )
    messages.success(request,"Η ενδιαφερόμενη επιχείρηση εγκρίθηκε με επιτυχία!")
    return redirect("list_espa_interested_businesses")

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def listSubsidizedBusinessView(request):
    if isStaff(request) or hasRole(request,"Associate"):
        businessobjects = SubsidizedBusiness.objects.order_by("-id")
    else:
        businessobjects = SubsidizedBusiness.objects.filter(referrer=request.user.espaassociate).order_by("-id")
    page = getPage(request, businessobjects, SubsidizedBusinessFilter)
    data = {
        'objects':page,
        'filter':SubsidizedBusinessFilter
    }
    return render(request,"Espa_Backend/Subsidized/list_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def addSubsidizedBusinessView(request):
    authorized = False
    if isStaff(request) or hasRole(request,"Associate"):
        authorized = True
    form = SubsidizedBusinessForm(authorized=authorized)
    data = {
        'form': form
    }
    if request.method == "POST":
        form = SubsidizedBusinessForm(request.POST)
        if form.is_valid():
            if SubsidizedBusiness.objects.filter(companyname=form.cleaned_data['companyname']).exists():
                return HttpResponse("The company already exists!")
                # return redirect("list_espa_subsidized_businesses")
            form.save()
            if request.POST.get("create_credentials") == "on":
                password = getRandomString(15)
                savedform = form.save(commit=False)
                addUser(
                    username=unidecode(form.cleaned_data['companyname']),
                    email=form.cleaned_data['email'],
                    password=password,
                    role='EspaUser'
                )
                savedform.user = User.objects.get(username=unidecode(form.cleaned_data['companyname']))
                if not authorized:
                    savedform.referrer = request.user.espaassociate
                savedform.save()
                sendEspaCredentials(
                    username=unidecode(form.cleaned_data['companyname']),
                    password=password,
                    email=form.cleaned_data['email'],
                    role="EspaUser"
                )
            messages.success(request, "Η επιχείρηση προστέθηκε επιτυχώς!")
            return redirect("list_espa_subsidized_businesses")
    return render(request,"Espa_Backend/Subsidized/add_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def editSubsidizedBusinessView(request,pk):
    authorized = False
    if isStaff(request) or hasRole(request, "Associate"):
        authorized = True
    instance = SubsidizedBusiness.objects.get(id=pk)
    form = SubsidizedBusinessForm(instance=instance,authorized=authorized)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = SubsidizedBusinessForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Τα στοιχεία της επιχείρησης άλλαξαν επιτυχώς!")
            return redirect('list_espa_subsidized_businesses')
    return render(request,"Espa_Backend/Subsidized/edit_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def deleteSubsidizedBusinessView(request,pk):
    instance = SubsidizedBusiness.objects.get(id=pk)
    data = {
        'instance': instance
    }
    if request.method == "POST":
        if instance.referrer == request.user:
            instance.delete()
            if instance.user:
                instance.user.delete()
            messages.success(request, "Η επιχείρηση διαγράφθηκε επιτυχώς!")
        else:
            messages.error(request,"Η επιχείρηση δεν μπόρεσε να διαγραφθεί!")
        return redirect("list_espa_subsidized_businesses")
    return render(request,"Espa_Backend/Subsidized/delete_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def viewSubsidizedBusinessView(request,pk):
    instance = SubsidizedBusiness.objects.get(id=pk)
    data = {
        'instance':instance
    }
    return render(request,"Espa_Backend/Subsidized/view_subsidized.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def documentsSubsidizedBusinessView(request,pk):
    company = SubsidizedBusiness.objects.get(id=pk)
    documentobjects = Document.objects.filter(company=SubsidizedBusiness.objects.get(id=pk)).order_by("-id")
    page = getPage(request,documentobjects,DocumentsBackendFilter)
    data = {
        'instance': page,
        'company': company
    }
    return render(request,"Espa_Backend/Subsidized/documents_subsidized.html",data)

@login_required(login_url="login")
@admin_only
def createEspaUserCredentials(request,pk):
    instance = SubsidizedBusiness.objects.get(id=pk)
    username = unidecode(instance.companyname)
    password = getRandomString(15)
    role = "EspaUser"
    addUser(
        username=username,
        password=password,
        email=instance.email,
        role=role
    )
    instance.user = User.objects.get(username=username)
    instance.save()
    sendEspaCredentials(
        username=username,
        password=password,
        email=instance.email,
        role=role
    )
    messages.success(request,"Τα στοιχεία πρόσβασης δημιουργήθηκαν επιτυχώς!")
    return redirect("list_espa_subsidized_businesses")

@login_required(login_url="login")
@admin_only
def removeEspaUserCredentials(request,pk):
    user = EspaAssociate.objects.get(id=pk).user
    user.delete()
    return

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def listServicesView(request):
    serviceobjects = EspaService.objects.order_by("-id")
    page = getPage(request, serviceobjects, ServicesFilter)
    data = {
        'objects':page,
        'filter':ServicesFilter
    }
    return render(request,"Espa_Backend/Services/list_services.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate'])
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
    return render(request,"Espa_Backend/Services/add_service.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate'])
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
    return render(request,"Espa_Backend/Services/edit_service.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate'])
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
        'filter':AssociatesFilter,
        'isAdmin':isAdmin(request)
    }
    return render(request,"Espa_Backend/Associates/list_associates.html",data)

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
    return render(request, "Espa_Backend/Associates/add_associate.html", data)

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
    return render(request,"Espa_Espa_Backend/Associates/edit_associate.html",data)

@login_required(login_url="login")
@staff_only
def deleteEspaAssociateView(request,pk):
    instance = EspaAssociate.objects.get(id=pk)
    instance.delete()
    if instance.user:
        instance.user.delete()
    messages.success(request, "Ο συνεργάτης διαγράφθηκε επιτυχώς!")
    return redirect("list_espa_associates")

@login_required(login_url="login")
@admin_only
def createEspaAssociateCredentials(request,pk):
    associateinstance = EspaAssociate.objects.get(id=pk)
    username = unidecode(associateinstance.associatename)
    password = getRandomString(15)
    role = "EspaAssociate"
    addUser(
        username=username,
        password=password,
        email=associateinstance.email,
        role=role
    )
    associateinstance.user = User.objects.get(username=username)
    associateinstance.save()
    sendEspaCredentials(username=username,password=password,email=associateinstance.email,role=role)
    return redirect("list_espa_associates")

@login_required(login_url="login")
@admin_only
def removeEspaAssociateCredentials(request,pk): #fix this to delete only user not the whole model using signals
    user = EspaAssociate.objects.get(id=pk).user
    user.delete()
    return redirect("list_espa_associates")

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def inspectDocumentView(request,pk):
    instance = Document.objects.get(id=pk)
    if instance.inspected is False:
        instance.inspected = True
        instance.save()
        messages.success(request, "Το έγγραφο ορίστηκε ως επιθεωρημένο ειτυχώς!")
    elif instance.inspected is True:
        instance.inspected = False
        instance.save()
        messages.success(request, "Το έγγραφο ορίστηκε ως μη επιθεωρημένο ειτυχώς!")
    return redirect("documents_espa_subsidized_businesses",instance.company.id)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def deleteDocument(request,pk):
    instance = Document.objects.get(id=pk)
    if instance.company.referrer == request.user.espaassociate or isStaff(request) or hasRole(request,"EspaAssociate"):
        os.remove(instance.file.path)
        instance.delete()
        messages.success(request,"Το έγγραφο διαγράφθηκε με επιτυχία!")
    else:
        messages.error(request,"Το έγγραφο δεν διαγράφθηκε!")
    return redirect("documents_espa_subsidized_businesses",instance.company.id)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Associate','EspaAssociate'])
def addDocumentView(request,pk):
    form = UploadDocumentBackendForm()
    data = {
        'form':form
    }
    if request.method == "POST":
        form = UploadDocumentBackendForm(request.POST,request.FILES)
        if form.is_valid():
            savedform = form.save(commit=False)
            savedform.company = SubsidizedBusiness.objects.get(id=pk)
            savedform.save()
            messages.success(request,"Το έγγραφο προστέθηκε με επιτυχία!")
            return redirect("list_espa_subsidized_businesses")
    return render(request,"Espa_Backend/Subsidized/add_document.html",data)

#Frontend
@login_required(login_url="login")
@allowed_roles(total_roles=["EspaUser"])
def homePageView(request):
    data = {

    }
    return render(request,"Espa_Frontend/Subsidized/home_page.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["EspaUser"])
def listDocuments(request):
    objects = Document.objects.filter(company=request.user.subsidizedbusiness).order_by("-id")
    data = {
        'objects':objects,
    }
    return render(request,"Espa_Frontend/Subsidized/list_documents.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["EspaUser"])
def uploadDocuments(request):
    form = UploadDocumentForm()
    data = {
        'form':form
    }
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploadEspaDocumentFiles(request)
            messages.success(request,"Τα αρχεία ανέβηκαν επιτυχώς!")
            return redirect('espauser_list_documents')
    return render(request,"Espa_Frontend/Subsidized/upload_documents.html",data)