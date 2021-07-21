from django.shortcuts import render
from assets.decorators.decorators import staff_only,allowed_roles
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from assets.functions.authentication import addUser
from django.contrib.auth.models import User
from .models import Teacher
from django.shortcuts import redirect
from .forms import TeacherModelForm
from students.forms import ExamModelForm
from students.models import Exam
from .models import SubjectReport,AttendanceReport
from assets.functions.authentication import hasRole,isStaff
from assets.functions.crypto import getRandomString
from unidecode import unidecode
from assets.functions.mailer import sendTeacherCredentials
from assets.functions.pagination import getPage
from .filters import *

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
            messages.success(request, "Ο καθηγητής προστέθηκε επιτυχώς!")
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
            messages.success(request,"Τα στοιχεία του καθηγητή άλλαξαν με επιτυχία!")
            return redirect("list_teachers")
    return render(request,"Teachers_Backend/Teacher/edit_teacher.html",data)

@login_required(login_url="login")
@staff_only
def deleteTeacherView(request,pk):
    instance = Teacher.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Ο Καθηγητής Διαγράφθηκε Με Επιτυχία!")
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
    messages.success(request, "Τα στοιχεία πρόσβασης δημιουργήθηκαν επιτυχώς!")
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
    messages.success(request,"Τα στοιχεία στάλθηκαν στην διεύθυνση email με επιτυχία!")
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
def addExamView(request):
    form = ExamModelForm
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ExamModelForm(request.POST)
        if form.is_valid():
            savedform = form.save(commit=False)
            savedform.teacher = request.user.teacher
            savedform.save()
    return render(request,"Teachers_Frontend/Exam/add_exam_grades.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def editExamView(request,pk):
    data = {

    }
    return render(request,"Teachers_Frontend/Exam/edit_exam_grades.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def listExamView(request):
    user = request.user.teacher
    if isStaff(request):
        objects = Exam.objects.all()
    else:
        objects = Exam.objects.filter(teacher=user)
    data = {
        'user':user,
        'objects':objects,
    }
    return render(request,"Teachers_Frontend/Exam/teachers_exams.html",data)

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
    data = {

    }
    return render(request,"Teachers_Frontend/SubjectReport/add_report.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def editSubjectReportView(request,pk):
    instance = SubjectReport.objects.get(id=pk)
    data = {}
    if instance.teacher == request.user.teacher:
        data = {

        }
    return render(request,"Teachers_Frontend/SubjectReport/edit_report.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def deleteSubjectReportView(request,id):
    data = {

    }
    return render(request,"Teachers_Frontend/SubjectReport/delete_report.html",data)

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
    data = {

    }
    return render(request,"Teachers_Frontend/AttendanceBook/add_attendance.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def editAttendanceReportView(request,pk):
    data = {

    }
    return render(request,"Teachers_Frontend/AttendanceBook/edit_attendance.html",data)

@login_required(login_url="login")
@allowed_roles(total_roles=["Admin","Staff","Teacher"])
def deleteAttendanceReportView(request,pk):
    data = {

    }
    return render(request,"Teachers_Frontend/AttendanceBook/delete_attendance.html",data)