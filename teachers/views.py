from django.shortcuts import render
from assets.decorators.decorators import staff_only,allowed_roles
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from administrator.functions.auth import addUser,assignToGroup
from django.contrib.auth.models import User
from .models import Teacher
from django.shortcuts import redirect
from .forms import TeacherModelForm
from students.forms import ExamModelForm
from students.models import Exam
from .models import SubjectReport,AttendanceReport
from assets.functions.authentication import getUserDetails
from assets.functions.crypto import getRandomString
from django.core.mail import send_mail

#Backend
@login_required(login_url="login")
@staff_only
def listTeachersView(request):
    objects = Teacher.objects.all()
    data = {
        'objects':objects
    }
    return render(request, "Backend/Teachers/list_teachers.html", data)

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
            savedform = form.save(commit=False)
            password = getRandomString(string_length=10)
            addUser(username=request.POST['username'],email=request.POST['email'],password=password)
            assignToGroup(request.POST['username'],'Teacher')
            savedform.user = User.objects.get(username=request.POST['username'])
            savedform.save()
            # send_mail(
            #     "Λογαριασμός στο σύστημα της Millenium",
            #     "Δημιουργήθηκε με επιτυχία ο λογαριασμός σας με τα παρακάτω στοιχεία:\nΌνομα Χρήστη: " + request.POST['username'] + "\nΚωδικός Πρόσβασης: " + password
            #     ["email@localhost"],
            #     request.POST['email']
            # )
            messages.success(request, "Ο καθηγητής προστέθηκε επιτυχώς!")
            return redirect("list_teachers")
    return render(request, "Backend/Teachers/add_teacher.html", data)

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

    return render(request,"Backend/Teachers/edit_teacher.html",data)

@login_required(login_url="login")
@staff_only
def deleteTeacherView(request,pk):
    forminstance = Teacher.objects.get(id=pk)
    data = {
        'forminstance':forminstance
    }
    if request.method == "POST":
        forminstance.delete()
        messages.success(request,"Ο Καθηγητής Διαγράφθηκε Με Επιτυχία!")
        return redirect("list_teachers")
    return render(request,"Backend/Teachers/delete_teacher.html",data)

#Frontend
@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherHomeView(request):
    data = {

    }
    return render(request,"Frontend/Teachers/teachers_home.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherAddExamView(request):
    form = ExamModelForm
    # user = getUserRole(request)
    user = None
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ExamModelForm(request.POST)
        if form.is_valid():
            savedform = form.save(commit=False)
            savedform.teacher = user
            savedform.save()
    return render(request,"Frontend/Exams/add_exam_grades.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherEditExamView(request):
    data = {

    }
    return render(request,"Frontend/Exams/edit_exam_grades.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherExamsView(request):
    user = getUserDetails(request)
    if hasattr(request.user,"teacher"):
        objects = Exam.objects.filter(teacher=user)
    else:
        objects = None
    data = {
        'user':user,
        'objects':objects,
    }
    return render(request,"Frontend/Exams/teachers_exams.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherReportListView(request):
    user = getUserDetails(request)
    if usertype == "Teacher":
        objects = SubjectReport.objects.filter(teacher=user)
    elif usertype == "Admin" or usertype == "Staff":
        objects = SubjectReport.objects.all()
    else:
        objects = None
    data = {
        'objects':objects
    }
    return render(request,"Frontend/DailyReports/list_reports.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherAddReportView(request):
    data = {

    }
    return render(request,"Frontend/DailyReports/add_report.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherEditReportView(request,id):
    data = {

    }
    return render(request,"Frontend/DailyReports/edit_report.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherDeleteReportView(request,id):
    data = {

    }
    return render(request,"Frontend/DailyReports/delete_report.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherAttendanceListView(request):
    user = getUserDetails(request)
    objects = None
    # if usertype == "Teacher":
    #     objects = AttendanceReport.objects.filter(teacher=user)
    # elif usertype == "Admin" or usertype == "Staff":
    #     objects = AttendanceReport.objects.all()
    # else:
    #     objects = None
    data = {
        'objects':objects
    }
    return render(request,"Frontend/AttendanceBook/list_attendances.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherAddAttendanceView(request):
    data = {

    }
    return render(request,"Frontend/AttendanceBook/add_attendance.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherEditAttendanceView(request,id):
    data = {

    }
    return render(request,"Frontend/AttendanceBook/edit_attendance.html",data)

@login_required(login_url="login")
@allowed_roles(roles=["Teacher"])
def teacherDeleteAttendanceView(request,id):
    data = {

    }
    return render(request,"Frontend/AttendanceBook/delete_attendance.html",data)