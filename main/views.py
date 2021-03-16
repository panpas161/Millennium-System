from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from assets.decorators.decorators import staff_only,homeRedirect

@login_required(login_url="login")
@homeRedirect
@staff_only
def homeView(request):
    data = {

    }
    return render(request,"home.html",data)