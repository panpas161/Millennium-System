from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from .models import Student, Specialty, Installment,Department,Exam
from .forms import StudentModelForm, SpecialtyModelForm, VoucherModelForm,DepartmentModelForm
from .getstudentobjects import getInstallmentsIDS,getInstallmentsPaidSum
from Millennium_System import settings
from .filters import StudentFilter
from django.contrib import messages
from administrator.functions.auth import addUser,assignToGroup
from .functions.departments import getSelectedDays,getSelectedTeachers,getSelectedDuration,getSelectedStartTime,getSelectedEndTime
from assets.functions.users import getUserID,getStudentID
from assets.decorators.decorators import staff_only,allowed_roles
from staff.models import Staff

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

@login_required(login_url="login")
@staff_only
def addStudentView(request):#IMPORTANT: FIX THAT INSTALLMENT THING,id is removed so remove next_id and if installments == 0
    form = StudentModelForm
    installments = Installment
    voucherform = VoucherModelForm
    data = {
        'studentmodel': form,
        'vouchermodel':voucherform
    }
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            price = int(request.POST.get("price"))
            #check if prokataboli is set
            if request.POST.get("prokataboli") != "":
                prokataboli = int(request.POST.get("prokataboli"))
            else:
                prokataboli = 0
            if request.POST.get("discount") != "":
                discount = int(request.POST.get("discount"))
            else:
                discount = 0
            installment_number = int(request.POST.get("installment_number"))
            amount_per_installment = (price - prokataboli - discount) / installment_number
            idnum = request.POST.get("id")
            try:
                next_id = Installment.objects.order_by("-id").first().id + 1
            except:
                next_id = 0
            for i in range(0, installment_number):
                if i == 0:
                    #if installment number is 1 then don't set the first installment as prokataboli
                    if installment_number != 1:
                        #if prokataboli is 0 set first installment as paid
                        if prokataboli != 0:
                            installments = Installment(id=next_id,student=Student.objects.get(pk=idnum), payment_number=i + 1,amount=prokataboli,date=settings.CURRENT_DATE, paid=False)
                        else:
                            installments = Installment(id=next_id,student=Student.objects.get(pk=idnum), payment_number=i + 1,amount=prokataboli,date=settings.CURRENT_DATE, paid=True)
                    else:
                        #if prokataboli is set then add 2 installments
                        if prokataboli != 0:
                            installments = Installment(id=next_id, student=Student.objects.get(pk=idnum),
                                                       payment_number=i + 1, amount=amount_per_installment, date=settings.CURRENT_DATE,
                                                       paid=False)
                else:
                    next_id = Installment.objects.order_by("-id").first().id + 1
                    installments = Installment(id=next_id,student=Student.objects.get(pk=idnum), payment_number=i + 1,amount=amount_per_installment,date=settings.CURRENT_DATE, paid=False)
                installments.save()
            form.save()
            return redirect("list-students")
    return render(request, "Backend/Students/add_student.html", data)

@login_required(login_url="login")
@staff_only
def editStudentView(request, pk):
    studentinstance = Student.objects.get(id=pk)
    form = StudentModelForm(instance=studentinstance)
    data = {
        'form': form,
    }
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=studentinstance)
        if form.is_valid():
            form.save()
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
        "imagepath": "student_images/" + str(pk) + ".jpg",
        "studid":studentinstance.id,
        "lastname": studentinstance.lastname.upper(),
        "firstname": studentinstance.firstname.upper(),
        "fathersname":studentinstance.fathersname.upper(),
        "birthdate":studentinstance.birthdate,
        "afm":studentinstance.afm.upper(),
        "adt":studentinstance.adt.upper(),
        "location":studentinstance.location.upper(),
        #"sex":studentinstance.sex.upper(), remove null
        "voucher":studentinstance.voucher,
        "phonenumber":studentinstance.phonenumber,
        "cellphone":studentinstance.cellphone,
        "email":studentinstance.email,
        #"mothersname":studentinstance.mothersname.upper(), remove null
        "specialty":studentinstance.specialty.all()[0].specialty.upper(),
        "specialty_code":studentinstance.specialty.all()[0].code.upper(),
        "specialty_duration":studentinstance.specialty.all()[0].duration,
        "specialty_price":studentinstance.specialty.all()[0].price,
        #"specialty_discount":studentinstance.specialty.all()[0].discount,
        "specialty_total_price":int(studentinstance.specialty.all()[0].price),
        "student_price":studentinstance.price,
        "student_discount":studentinstance.discount,
        "student_total_price":studentinstance.price - studentinstance.discount,
        "installments_paid_sum":getInstallmentsPaidSum(pk),
    }
    return render(request,"Backend/Miscellaneous/installments_tab.html",data)

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
            return redirect("list_specialties")
    return render(request, "Backend/Specialties/add_specialty.html", data)

@login_required(login_url="login")
@staff_only
def editSpecialtiesView(request, pk):
    specialtiesinstance = Specialty.objects.get(id=pk)
    form = SpecialtyModelForm(instance=specialtiesinstance)
    data = {
        'edit_form': form,
        'specialty': specialtiesinstance.specialty
    }
    if request.method == "POST":
        form = SpecialtyModelForm(request.POST, instance=specialtiesinstance)
        if form.is_valid():
            form.save()
            messages.success(request, "Τα στοιχεία της ειδικότητας άλλαξαν επιτυχώς!")
            return redirect('list_specialties')
    return render(request, "Backend/Specialties/edit_specialty", data)

@login_required(login_url="login")
@staff_only
def getInstallmentsView(request,pk):#delete
    data = {
        'installments_list':getInstallmentsIDS(pk)
    }
    return render(request,"Backend/Installments/get_installments.html",data)

@login_required(login_url="login")
@staff_only
def listDepartmentsView(request):
    objects = Department.objects.all().order_by("-id")
    data = {
        'objects':objects
    }
    return render(request,"Backend/Departments/list_departments.html",data)

@login_required(login_url="login")
@staff_only
def addDepartmentView(request):
    form = DepartmentModelForm()
    data = {
        'form':form
    }
    if request.method == "POST":
        selected_days = getSelectedDays(request)
        selected_teachers = getSelectedTeachers(request)
        selected_start_time = getSelectedStartTime(request)
        selected_end_time = getSelectedEndTime(request)
        selected_durations = getSelectedDuration(request)
        for i in range(0,len(selected_days)):
                if selected_days[i] is not None:
                    departments = Department(id=i,departmentname=Specialty.objects.get(id=request.POST['departmentname']),teacher=selected_teachers[i],
                                                program=request.POST['program'],start_time=selected_start_time[i],end_time=selected_end_time[i],
                                               duration=selected_durations[i],weekday=selected_days[i],entrydate=settings.CURRENT_DATE)
                    departments.save()
                    messages.success(request,"Το τμήμα προστέθηκε επιτυχώς!")
                    return redirect("list-students")

    return render(request,"Backend/Departments/add_department.html",data)
#frontend
@login_required(login_url="login")
@allowed_roles(roles=["Student"])
def mainStudentView(request):
    data = {

    }
    return render(request,"Frontend/Students/menu_page.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Student"])
def installmentsFrontTabView(request):
    try:
        user = Student.objects.get(user=getUserID(request.user))
        data = {
            'user': user,
        }
    except Exception:
        data = {
            'user': 'user'
        }
    return render(request,"Frontend/Students/installments_tab.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Student"])
def examsStudentView(request):
    try:
        objects = Exam.objects.filter(student=getStudentID(request.user))
        data = {
            'objects': objects
        }
    except Exception:
        data = {}
    return render(request,"Frontend/Students/exams_tab.html",data)

