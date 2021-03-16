from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .filters import UserFilter
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def homePageView(request):
    data = {

    }
    return render(request,"UI/home_page.html",data)

def editUserView(request,pk):
    data = {

    }
    return render(request,"Users/edit_user.html",data)

def listUsersView(request):
    objects = User.objects.all()
    filter = UserFilter(request.GET,queryset=objects)
    objects = filter.qs
    p = Paginator(objects,15)
    page_get = request.GET.get("page")
    try:
        page = p.page(page_get)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        return HttpResponse("Η σελίδα δεν βρέθηκε!")
    data = {
        'objects':objects
    }
    return render(request,"Users/list_users.html",data)

def addUserView(request,pk):
    data = {

    }
    return render(request,"Users/add_user.html",data)