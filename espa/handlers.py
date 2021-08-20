from .models import Document
from django.contrib import messages

def uploadEspaDocumentFiles(request,company):
    files = request.FILES.getlist('file')
    for file in files:
        if file.content_type == "application/pdf":
            Document(
                file=file,
                comments=request.POST.get("comments"),
                company=company
            ).save()
        else:
            messages.error(request,"Τα αρχεία πρέπει να εχούν την μορφή pdf!")