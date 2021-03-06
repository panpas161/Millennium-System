from django.shortcuts import render
from assets.decorators.decorators import staff_only,allowed_roles,staff_and_roles
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from assets.functions.authentication import addUser
from django.shortcuts import redirect
from .forms import TeacherModelForm
from students.forms import ExamGradeForm
from students.models import ExamGrade,Department,DepartmentDay
from students.filters import ExamGradeFilter,ExamGradeStaffFilter
from .models import *
from assets.functions.authentication import isStaff
from assets.functions.crypto import getRandomString
from unidecode import unidecode
from assets.functions.mailer import sendTeacherCredentials
from assets.functions.pagination import getPage
from .filters import *
from .forms import *
from django.http import JsonResponse
from django.shortcuts import HttpResponse

#Backend
@login_required(login_url="login")
@staff_only
def listTeachersView(request):
    objects = Teacher.objects.all().order_by("-id")
    page = getPage(request,objects,TeacherFilter)
    data = {
        'objects':page,
        'filter':TeacherFilter
    }
    return render(request, "Teachers_Backend/Teacher/list_teachers.html", data)

@login_required(login_url="login")
@staff_only
def addTeacherView(request):
    form = TeacherModelForm()
    data = {
        'form': form
    }
    if request.method == "POST":
        form = TeacherModelForm(request.POST)
        if form.is_valid():
            username = unidecode(form.cleaned_data['firstname'])[0] + unidecode(form.cleaned_data['lastname'])
            savedform = form.save(commit=False)
            password = getRandomString(15)
            addUser(
                username=username,
                email=form.cleaned_data['email'],
                password=password,
                role="Teacher"
            )
            savedform.user = User.objects.get(username=username)
            savedform.save()
            sendTeacherCredentials(
                username=username,
                password=password,
                email=form.cleaned_data['email']
            )
            messages.success(request, "?? ?????????????????? ???????????????????? ????????????????!")
            return redirect("list_teachers")
    return render(request, "Teachers_Backend/Teacher/add_teacher.html", data)

@login_required(login_url="login")
@staff_only
def editTeacherView(request,pk):
    forminstance = Teacher.objects.get(id=pk)
    form = TeacherModelForm(instance=forminstance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = TeacherModelForm(request.POST,instance=forminstance)
        if form.is_valid():
            form.save()
            messages.success(request,"???? ???????????????? ?????? ???????????????? ?????????????? ???? ????????????????!")
            return redirect("list_teachers")
    return render(request,"Teachers_Backend/Teacher/edit_teacher.html",data)

@login_required(login_url="login")
@staff_only
def deleteTeacherView(request,pk):
    instance = Teacher.objects.get(id=pk)
    instance.delete()
    messages.success(request,"?? ?????????????????? ?????????????????????? ???? ????????????????!")
    return redirect("list_teachers")

@login_required(login_url="login")
@staff_only
def createTeacherCredentials(request,pk):
    instance = Teacher.objects.get(id=pk)
    username = unidecode(instance.firstname)[0] + unidecode(instance.lastname)
    password = getRandomString(15)
    role = "Teacher"
    addUser(
        username=username,
        password=password,
        email=instance.email,
        role=role
    )
    instance.save()
    sendTeacherCredentials(
        username=username,
        password=password,
        email=instance.email,
        role=role
    )
    messages.success(request, "???? ???????????????? ?????????????????? ???????????????????????????? ????????????????!")
    return redirect("list-teachers")

@login_required(login_url="login")
@staff_only
def recreateTeacherCredentials(request,pk):
    instance = Teacher.objects.get(id=pk)
    user = instance.user
    password = getRandomString(15)
    user.set_password(password)
    user.save()
    sendTeacherCredentials(
        username=user.username,
        password=password,
        email=instance.email,
        role="Teacher"
    )
    messages.success(request,"???? ???????????????? ?????????????????? ???????? ?????????????????? email ???? ????????????????!")
    return redirect("list-teachers")

#Frontend
@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def teacherHomeView(request):
    data = {

    }
    return render(request,"Teachers_Frontend/Main/teachers_home.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def addExamGradeView(request):
    authorized = False
    if isStaff(request):
        authorized = True
    form = ExamGradeForm(authorized=authorized)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ExamGradeForm(request.POST)
        if form.is_valid():
            if isStaff(request):
                form.save()
            else:
                savedform = form.save(commit=False)
                savedform.teacher = request.user.teacher
                savedform.save()
    return render(request,"Teachers_Frontend/ExamGrade/add_exam_grade.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def editExamGradeView(request,pk):
    instance = ExamGrade.objects.get(id=pk)
    form = ExamGradeForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ExamGradeForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,"")
            return redirect("list_teachers_exam_grades")
    return render(request,"Teachers_Frontend/ExamGrade/edit_exam_grade.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def listExamGradeView(request):
    if isStaff(request):
        page_filter = ExamGradeStaffFilter
        objects = ExamGrade.objects.all()
        page = getPage(request,objects,page_filter)
    else:
        page_filter = ExamGradeFilter
        objects = ExamGrade.objects.filter(teacher=request.user.teacher)
        page = getPage(request,objects,page_filter)
    data = {
        'user':request.user,
        'objects':page,
        'filter':page_filter
    }
    return render(request,"Teachers_Frontend/ExamGrade/list_exam_grades.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def listSubjectReportView(request):
    if isStaff(request):
        objects = SubjectReport.objects.all()
    else:
        objects = SubjectReport.objects.filter(teacher=request.user.teacher)
    data = {
        'objects':objects
    }
    return render(request,"Teachers_Frontend/SubjectReport/list_reports.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def addSubjectReportView(request):
    authorized = False
    if isStaff(request):
        authorized = True
    form = SubjectReportForm(authorized=authorized)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = SubjectReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"")
            return redirect("list_teachers_subject_reports")
    return render(request,"Teachers_Frontend/SubjectReport/add_report.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def editSubjectReportView(request,pk):
    authorized = False
    if isStaff(request):
        authorized = True
    instance = SubjectReport.objects.get(id=pk,authorized=authorized)
    data = {}
    if instance.teacher == request.user.teacher:
        data = {

        }
    return render(request,"Teachers_Frontend/SubjectReport/edit_report.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def deleteSubjectReportView(request,pk):
    instance = SubjectReport.objects.get(id=pk)
    instance.delete()
    messages.success(request,"???? ???????????? ?????????????????? ?????????????????????? ????????????????!")
    return render(request,"Teachers_Frontend/SubjectReport/delete_report.html")

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def listAttendanceReportView(request):
    if isStaff(request):
        objects = AttendanceReport.objects.all()
    else:
        objects = AttendanceReport.objects.filter(teacher=request.user.teacher)
    data = {
        'objects':objects
    }
    return render(request,"Teachers_Frontend/AttendanceBook/list_attendances.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def addAttendanceReportView(request):
    authorized = False
    if isStaff(request):
        authorized = True
    form = AttendanceReportForm(authorized=authorized)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = AttendanceReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"???? ???????????? ?????????????????? ???????????????????? ????????????????!")
            return redirect("list_teachers_attendance_reports")
    return render(request,"Teachers_Frontend/AttendanceBook/add_attendance.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def editAttendanceReportView(request,pk):
    instance = AttendanceReport.objects.get(id=pk)
    form = SubjectReportForm(instance=instance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = SubjectReportForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,"???? ???????????????? ?????? ?????????????? ?????????????????? ?????????????? ????????????????!")
            return redirect("list_teachers_subject_report")
    return render(request,"Teachers_Frontend/AttendanceBook/edit_attendance.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def deleteAttendanceReportView(request,pk):
    instance = AttendanceReport.objects.get(id=pk)
    instance.delete()
    messages.success(request,"???? ???????????? ?????????????????? ?????????????????????? ????????????????!")
    return render(request,"Teachers_Frontend/AttendanceBook/delete_attendance.html")


@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Teacher'])
def getTeacherDepartments(request,teacherpk):
    #authentication checks
    if hasattr(request.user,'teacher'): #or hasrole
        if request.user.teacher.id != int(teacherpk):
            return HttpResponse("?????? ?????????????????????? ?? ????????????????")
    teacher = Teacher.objects.get(id=teacherpk)
    departments = {}
    for day in DepartmentDay.objects.all().filter(teacher=teacher):
        departments.update(day.getDepartment())
    #remove duplicates
    # departments = dict.fromkeys(departments)
    return JsonResponse(departments,safe=False)

@login_required(login_url="login")
@allowed_roles(total_roles=['Admin','Staff','Teacher'])
def getTeacherStudents(request,departmentpk):
    department = Department.objects.get(id=departmentpk)
    #authentication checks
    # if hasattr(request.user,'teacher'): #or hasrole
        # if request.user.teacher.id in department.departmentday_set.all()
    students = department.getParticipants()
    data = {
        'students':students
    }
    return JsonResponse(data)