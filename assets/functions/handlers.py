def handle_uploaded_file(f,path):
    with open('./uploads/'+path,"wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)