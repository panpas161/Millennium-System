from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from .models import *
from .forms import *
from Millennium_System import settings
from .filters import *
from django.contrib import messages
from assets.decorators.decorators import staff_only,allowed_roles
from .functions.installments import calculateInstallments

@login_required(login_url="login")
@staff_only
def listStudentsView(request):
    studentobjects = Student.objects.order_by("-id")
    page_get = request.GET.get("page")
    studentfilter = StudentFilter(request.GET, queryset=studentobjects)
    studentobjects = studentfilter.qs
    #pagination
    p = Paginator(studentobjects,5)
    try:
        page = p.page(page_get)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        return HttpResponse("Η σελίδα δεν βρέθηκε!")
    data = {
        'objects':page,
        'filter':studentfilter,
    }
    return render(request, "Backend/Students/list_students.html", data)

# @login_required(login_url="login")
# @staff_only
# def addStudentView(request):#IMPORTANT: FIX THAT INSTALLMENT THING,id is removed so remove next_id and if installments == 0
#     form = StudentModelForm
#     installments = Installment
#     voucherform = VoucherModelForm
#     data = {
#         'studentmodel': form,
#         'vouchermodel':voucherform
#     }
#     if request.method == "POST":
#         form = StudentModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             price = int(request.POST.get("price"))
#             #check if prokataboli is set
#             if request.POST.get("prokataboli") != "":
#                 prokataboli = int(request.POST.get("prokataboli"))
#             else:
#                 prokataboli = 0
#             if request.POST.get("discount") != "":
#                 discount = int(request.POST.get("discount"))
#             else:
#                 discount = 0
#             installment_number = int(request.POST.get("installment_number"))
#             amount_per_installment = (price - prokataboli - discount) / installment_number
#             idnum = request.POST.get("id")
#             try:
#                 next_id = Installment.objects.order_by("-id").first().id + 1
#             except:
#                 next_id = 0
#             for i in range(0, installment_number):
#                 if i == 0:
#                     #if installment number is 1 then don't set the first installment as prokataboli
#                     if installment_number != 1:
#                         #if prokataboli is 0 set first installment as paid
#                         if prokataboli != 0:
#                             installments = Installment(id=next_id,student=Student.objects.get(pk=idnum), payment_number=i + 1,amount=prokataboli,date=settings.CURRENT_DATE, paid=False)
#                         else:
#                             installments = Installment(id=next_id,student=Student.objects.get(pk=idnum), payment_number=i + 1,amount=prokataboli,date=settings.CURRENT_DATE, paid=True)
#                     else:
#                         #if prokataboli is set then add 2 installments
#                         if prokataboli != 0:
#                             installments = Installment(id=next_id, student=Student.objects.get(pk=idnum),
#                                                        payment_number=i + 1, amount=amount_per_installment, date=settings.CURRENT_DATE,
#                                                        paid=False)
#                 else:
#                     next_id = Installment.objects.order_by("-id").first().id + 1
#                     installments = Installment(id=next_id,student=Student.objects.get(pk=idnum), payment_number=i + 1,amount=amount_per_installment,date=settings.CURRENT_DATE, paid=False)
#                 installments.save()
#             form.save()
#             return redirect("list-students")
#     return render(request, "Backend/Students/add_student.html", data)

def addStudentView(request):
    studentform = StudentModelForm
    voucherform = VoucherModelForm
    vouchersame = False
    if request.GET.get("vouchersame"):
        vouchersame = True
    data = {
        'studentform':studentform,
        'voucherform':voucherform,
        'vouchersame':vouchersame,
    }
    if request.method == "POST":
        studentform = StudentModelForm(request.POST)
        voucherform = VoucherModelForm(request.POST)
        if studentform.is_valid():
            studentinstance = studentform.save(commit=False)
            if not vouchersame:
                if voucherform.is_valid():
                    voucherinstance = voucherform.save()
                    studentinstance.voucher = voucherinstance
            studentinstance.save()
            # calculateInstallments(
            #     int(request.POST.get("price")),
            #     int(request.POST.get("discount")),
            #     int(request.POST.get("prokataboli")),
            #     int(request.POST.get("installment_number")),
            #     studentinstance
            # )
            messages.success(request, "Ο μαθητής προστέθηκε με επιτυχία!")
            return redirect("list-students")
    return render(request, "Backend/Students/add_student.html",data)

@login_required(login_url="login")
@staff_only
def editStudentView(request, pk):
    studentinstance = Student.objects.get(id=pk)
    studentform = StudentModelForm(instance=studentinstance)
    voucherinstance = None
    if studentinstance.voucher:
        voucherinstance = studentinstance.voucher
    voucherform = VoucherModelForm(instance=voucherinstance)
    data = {
        'studentform': studentform,
        'voucherform':voucherform
    }
    if request.method == "POST":
        studentform = StudentModelForm(request.POST, instance=studentinstance)
        voucherform = VoucherModelForm(request.POST,instance=voucherinstance)
        if studentform.is_valid():
            studentform.save()
        if voucherform.is_valid():
            voucherform.save()
        messages.success(request, "Τα στοιχεία του μαθητή άλλαξαν επιτυχώς!")
        return redirect('list-students')
    return render(request, "Backend/Students/edit_student.html", data)

@login_required(login_url="login")
@staff_only
def deleteStudentView(request, pk):
    studentinstance = Student.objects.get(id=pk)
    data = {
        'id': studentinstance.id,
        'firstname': studentinstance.firstname,
        'lastname': studentinstance.lastname,
        'fathersname': studentinstance.fathersname,
        'afm': studentinstance.afm,
        'adt': studentinstance.adt,
        'phonenumber': studentinstance.phonenumber,
        'email': studentinstance.location,
        'location': studentinstance.location
    }
    if request.method == "POST":
        studentinstance.delete()
        messages.success(request,"Ο Μαθητής Διαγράφθηκε Επιτυχώς!")
        return redirect('list-students')
    return render(request, "Backend/Students/delete_student.html", data)

@login_required(login_url="login")
@staff_only
def economicContractView(request, pk):
    studentinstance = Student.objects.get(id=pk)
    data = {
        'student_fullname': studentinstance.lastname.upper() + " " + studentinstance.firstname.upper(),
        'student_specialty': studentinstance.specialty
    }
    return render(request, "Backend/Students/Miscellaneous/economic_contract.html", data)

@login_required(login_url="login")
@staff_only
def studentCardView(request, pk):
    studentinstance = Student.objects.get(id=pk)
    data = {
        'id': pk,
        'photoname': pk + ".jpg",
        'firstname':studentinstance.firstname.upper(),
        'lastname':studentinstance.lastname.upper(),
        'specialty':studentinstance.specialty,
    }
    return render(request, "Backend/Miscellaneous/student_card.html", data)

@login_required(login_url="login")
@staff_only
def installmentsTabView(request, pk):
    studentinstance = Student.objects.get(id=pk)
    #if type(studentinstance.mothersname) != "string":#something like that
    #    mothersname = studentinstance.mothersname
    data = {
        "studentinstance":studentinstance,
        "student_price":studentinstance.price,
        "student_discount":studentinstance.discount,
        "student_total_price":studentinstance.price - studentinstance.discount,
    }
    return render(request,"Backend/Miscellaneous/installments_tab.html",data)

@login_required(login_url="login")
@staff_only
def uploadStudentPicture(request,pk):
    instance = Student.objects.get(id=pk)
    form = StudentUploadPictureForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = StudentUploadPictureForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,"Η φωτογραφία ανέβηκε επιτυχώς!")
            return redirect("list-students")
    return render(request,"Backend/Students/upload_student_photo.html",data)

@login_required(login_url="login")
@staff_only
def listSpecialtiesView(request):
    objects = Specialty.objects.all()
    data = {
        'objects': objects
    }
    return render(request, "Backend/Specialties/list_specialties.html", data)

@login_required(login_url="login")
@staff_only
def addSpecialtiesView(request):
    form = SpecialtyModelForm()
    data = {
        'form': form
    }
    if request.method == "POST":
        form = SpecialtyModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Η Ειδικότητα προστέθηκε επιτυχώς!")
            return redirect("list_student_specialties")
    return render(request, "Backend/Specialties/add_specialty.html", data)

@login_required(login_url="login")
@staff_only
def editSpecialtiesView(request, pk):
    instance = Specialty.objects.get(id=pk)
    form = SpecialtyModelForm(instance=instance)
    data = {
        'form': form,
        'instance': instance
    }
    if request.method == "POST":
        form = SpecialtyModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Τα στοιχεία της ειδικότητας άλλαξαν επιτυχώς!")
            return redirect('list_specialties')
    return render(request, "Backend/Specialties/edit_specialty.html", data)

@login_required(login_url="login")
@staff_only
def deleteSpecialtyView(request,pk):
    instance = Specialty.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Η ειδικότητα διαγράφθηκε επιτυχώς!")
    return redirect("delete_student_specialty")

@login_required(login_url="login")
@staff_only
def listDepartmentsView(request):
    objects = Department.objects.all().order_by("-id")
    data = {
        'objects':objects
    }
    return render(request,"Backend/Departments/list_departments.html",data)

# @login_required(login_url="login")
# @staff_only
# def addDepartmentView(request):
#     form = DepartmentModelForm()
#     data = {
#         'form':form
#     }
#     if request.method == "POST":
#         selected_days = getSelectedDays(request)
#         selected_teachers = getSelectedTeachers(request)
#         selected_start_time = getSelectedStartTime(request)
#         selected_end_time = getSelectedEndTime(request)
#         selected_durations = getSelectedDuration(request)
#         for i in range(0,len(selected_days)):
#                 if selected_days[i] is not None:
#                     departments = Department(id=i,departmentname=Specialty.objects.get(id=request.POST['departmentname']),teacher=selected_teachers[i],
#                                                 program=request.POST['program'],start_time=selected_start_time[i],end_time=selected_end_time[i],
#                                                duration=selected_durations[i],weekday=selected_days[i],entrydate=settings.CURRENT_DATE)
#                     departments.save()
#                     messages.success(request,"Το τμήμα προστέθηκε επιτυχώς!")
#                     return redirect("list-students")
#
#     return render(request,"Backend/Departments/add_department.html",data)

@login_required(login_url="login")
@staff_only
def addDepartmentView(request):
    form = DepartmentModelForm
    data = {
        'form':form
    }
    if request.method == "POST":
        form = DepartmentModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Το τμήμα δημιουργήθηκε επιτυχώς!")
            return redirect("list_student_departments")
    return render(request,"Backend/Departments/add_department_2.html",data)

@login_required(login_url="login")
@staff_only
def editDepartmentView(request,pk):
    instance = Department.objects.get(id=pk)
    form = DepartmentModelForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = DepartmentModelForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,"Οι αλλαγές πραγματοποιήθηκαν με επιτυχία!")
            return redirect("list_student_departments")
    return render(request,"Backend/Departments/edit_department.html",data)

@login_required(login_url="login")
@staff_only
def deleteDepartmentView(request,pk):
    instance = Department.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Το τμήμα διαγράφθηκε με επιτυχία!")
    return redirect("list_student_departments")

def createDepartmentScheduleView(request,pk):
    instance = Department.objects.get(id=pk)
    data = {

    }
    return render(request,"Backend/Students/create_schedule_department.html",data)
#frontend
@login_required(login_url="login")
@allowed_roles(total_roles=["Student"])
def mainStudentView(request):
    data = {

    }
    return render(request,"Frontend/Students/menu_page.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Student"])
def installmentsFrontTabView(request):
    try:
        user = Student.objects.get(user=request.user)
        data = {
            'user': user,
        }
    except Exception:
        data = {
            'user': 'user'
        }
    return render(request,"Frontend/Students/installments_tab.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Student"])
def examsStudentView(request):
    try:
        objects = ExamGrade.objects.filter(student=request.user.student)
        data = {
            'objects': objects
        }
    except Exception:
        data = {}
    return render(request,"Frontend/Students/exams_tab.html",data)

