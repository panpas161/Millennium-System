from django.shortcuts import render
from assets.decorators.decorators import staff_only,allowed_roles
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
@staff_only
def listSubsidizedBusinessView(request):
    data = {

    }
    return render(request,"Backend/Subsidized/list_subsidized.html",data)

@login_required(login_url="login")
@staff_only
def addSubsidizedBusinessView(request):
    data = {

    }
    return render(request,"Backend/Subsidized/add_subsidized.html",data)

@login_required(login_url="login")
@staff_only
def editSubsidizedBusinessView(request):
    data = {

    }
    return render(request,"Backend/Subsidized/edit_subsidized.html",data)

@login_required(login_url="login")
@staff_only
def deleteSubsidizedBusinessView(request):
    data = {

    }
    return render(request,"Backend/Subsidized/delete_subsidized.html",data)