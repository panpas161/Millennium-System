from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from .models import *
from .forms import *
from Millennium_System import settings
from .filters import *
from django.contrib import messages
from assets.decorators.decorators import staff_only,allowed_roles
from django.http import JsonResponse

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
def addStudentView(request):
    studentform = StudentModelForm
    voucherform = VoucherModelForm
    specialtiesform = MultiSpecialtiesForm({
        "form-TOTAL_FORMS": len(Specialty.objects.all()),
        "form-INITIAL_FORMS": len(Specialty.objects.all()),
        "form-MIN_NUM_FORMS": len(Specialty.objects.all()),
        "form-MAX_NUM_FORMS": len(Specialty.objects.all())
    })
    installmentsform = InstallmentForm
    vouchersame = False
    if request.GET.get("vouchersame"):
        vouchersame = True
    data = {
        'studentform':studentform,
        'voucherform':voucherform,
        'vouchersame':vouchersame,
        'installmentsform':installmentsform,
        'specialtiesform':specialtiesform,
        'specialties_len':len(Specialty.objects.all())
    }
    if request.method == "POST":
        studentform = StudentModelForm(request.POST)
        voucherform = VoucherModelForm(request.POST)
        specialtiesform = MultiSpecialtiesForm(request.POST)
        installmentsform = InstallmentForm(request.POST)
        if studentform.is_valid():
            studentinstance = studentform.save(commit=False)
            if not vouchersame:
                if voucherform.is_valid():
                    voucherinstance = voucherform.save()
                    if installmentsform.is_valid():
                        studentinstance.voucher = voucherinstance
            if installmentsform.is_valid():
                studentinstance.save()
                for specialtyform in specialtiesform:
                    if specialtyform.is_valid():
                        savedspecialty = specialtyform.save(commit=False)
                        savedspecialty.student = studentinstance
                        savedspecialty.save()
                installmentsform.save(student=studentinstance)
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
        # "student_price":studentinstance.price,
        # "student_discount":studentinstance.discount,
        # "student_total_price":studentinstance.price - studentinstance.discount,
    }
    return render(request,"Backend/Miscellaneous/installments_tab.html",data)

@login_required(login_url="login")
@staff_only
def printCertificateMenuView(request,pk):
    instance = Student.objects.get(id=pk)
    data = {
        'instance':instance
    }
    return render(request,"Backend/Miscellaneous/certificate_menu.html",data)

@login_required(login_url="login")
@staff_only
def printSeminarCertificateView(request,pk):
    instance = Student.objects.get(id=pk)
    form = SeminarCertificateForm()
    form.fields['firstname'].initial = instance.firstname
    form.fields['lastname'].initial = instance.lastname
    form.fields['sex'].initial = instance.sex
    form.fields['fathersname'].initial = instance.fathersname
    form.fields['adt'].initial = instance.adt
    form.fields['specialty'].initial = instance.specialty.name
    form.fields['location'].initial = instance.location
    data = {
        'form':form,
    }
    if request.method == "POST":
        form = SeminarCertificateForm(request.POST)
        if form.is_valid():
            formdata = {
                'postdata':form.cleaned_data
            }
            return render(request, "Backend/Miscellaneous/print_seminar_certificate.html",formdata)
    return render(request,"Backend/Miscellaneous/print_seminar_certificate_form.html",data)

@login_required(login_url='login')
@staff_only
def printCommendationCertificateView(request,pk):
    instance = Student.objects.get(id=pk)
    form = CommendationCertificateForm
    data = {
        'form':form
    }
    if request.method == "POST":
        form = CommendationCertificateForm(request.POST)
        if form.is_valid():
            formdata = {
                'postdata':form.cleaned_data
            }
            return render(request,"Backend/Miscellaneous/print_commendation_certificate.html",formdata)
    return render(request,"Backend/Miscellaneous/print_commendation_certificate_form.html",data)

@login_required(login_url="login")
@staff_only
def printPraiseCertificateView(request,pk):
    instance = Student.objects.get(id=pk)
    form = PraiseCertificateForm
    data = {
        'form':form
    }
    if request.method == "POST":
        form = PraiseCertificateForm(request.POST)
        if form.is_valid():
            formdata = {
                'postdata':form.cleaned_data
            }
            return render(request,"Backend/Miscellaneous/print_praise_certificate.html",formdata)
    return render(request,"Backend/Miscellaneous/print_praise_certificate_form.html",data)
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
    return render(request,"Backend/Departments/add_department.html",data)

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
    forms = DepartmentDayMultipleForm()
    hasvalidforms = False
    data = {
        'forms': forms,
        'instance': instance,
    }
    if request.method == "POST":
        forms = DepartmentDayMultipleForm(request.POST)
        for form in forms:
            if form.is_valid():
                savedform = form.save(commit=False)
                savedform.department = instance
                savedform.save()
                hasvalidforms = True
        if hasvalidforms:
            messages.success(request, "Το ωράριο δημιουργήθηκε με επιτυχία!")
        return redirect("list_student_departments")
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
        user = request.user.student
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
    objects = ExamGrade.objects.filter(student=request.user.student)
    data = {
        'objects': objects
    }
    return render(request,"Frontend/Students/exams_tab.html",data)

@login_required(login_url="login")
@staff_only
def getSpecialties(request):
    specialties = []
    for specialty in Specialty.objects.all():
        specialties.append(specialty.getJSONSpecialty())
    return JsonResponse(specialties,safe=False)

@login_required(login_url="login")
@staff_only
def getSpecialtyPrices(request):
    prices = {}
    for price in Specialty.objects.all():
        prices.update(price.getJSONPrice())
    return JsonResponse(prices)