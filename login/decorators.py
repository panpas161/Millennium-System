from django.shortcuts import redirect,render
from django.http import HttpResponse
def students_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.groups.values_list('Students', flat=True):
            return redirect('students_front_home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def forbidden_login_required(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.groups.values_list('Students', flat=True):
            return render(None,"error403")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func