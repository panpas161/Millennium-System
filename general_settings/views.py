from django.shortcuts import render

def showProfileView(request):
    data = {}
    return render(request,"Profiles/show_profile.html",data)

def editProfileView(request):
    data = {}
    return render(request,"Profiles/edit_profile.html",data)