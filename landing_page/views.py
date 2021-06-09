from django.shortcuts import render
from espa.forms import InterestedBusinessForm
from django.contrib import messages
from django.shortcuts import redirect

def espaMainView(request):
    data = {

    }
    return render(request,"Frontend/Espa/espa_landing_page.html",data)

def espaRegisterView(request):
    form = InterestedBusinessForm
    if request.method == "POST":
        form = InterestedBusinessForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Η αίτηση υποβλήθηκε με επιτυχία!")
            return redirect("landing_page_espa_lawyer")
    data = {
        'form': form
    }
    return render(request,"Frontend/Espa/espa_register.html",data)
