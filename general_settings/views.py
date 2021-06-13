from django.shortcuts import render

# Create your views here.

def editProfileView(request):
    data = {}
    return render(request,"Profiles/edit_profile.html",data)