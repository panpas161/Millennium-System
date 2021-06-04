from django.shortcuts import render

# Create your views here.

def espaPage1(request):
    data = {

    }
    return render(request,"Frontend/Espa/lawyer_page.html",data)

# def addInterestedBusiness(request):
#     if request.method == "POST":
#