from .models import Document
from django.shortcuts import HttpResponse

def uploadEspaDocumentFiles(request):
    files = request.FILES.getlist('file')
    for file in files:
        if file.content_type == "application/pdf":
            Document(
                file=file,
                comments=request.POST.get("comments"),
                company=request.user.subsidizedbusiness
            ).save()
        else:
            return HttpResponse("Τα αρχεία πρέπει να εχούν την μορφή pdf!")