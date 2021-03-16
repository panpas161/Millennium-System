from django.shortcuts import redirect
from django.contrib import messages

#does not redirect check it
def checkAddForm(request,modelform,message,redirectaddr):
    if request.method == "POST":
        form = modelform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,message)
            return redirect(redirectaddr)