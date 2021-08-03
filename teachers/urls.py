from django.urls import path
from .views import *

urlpatterns = [
    # backend
    path('list/', listTeachersView, name="list_teachers"),
    path('add/', addTeacherView, name="add_teacher"),
    path('edit/<str:pk>', editTeacherView, name="edit_teacher"),
    path('delete/<str:pk>', deleteTeacherView, name="delete_teacher"),
    path('credentials/create/<str:pk>', createTeacherCredentials, name="create_teacher_credentials"),
    path('credentials/create/new/<str:pk>', recreateTeacherCredentials, name="recreate_teacher_credentials"),
    #frontend
    path('home/', teacherHomeView, name="teacher_home_page"),
    path('exams/add/', addExamGradeView, name="add_teacher_grades"),
    path('exams/edit/<pk>', editExamGradeView, name="edit_teacher_grades"),
    path('exams/list', listExamGradeView, name="list_teacher_exams"),
    path('subject_reports/list', listSubjectReportView, name="list_teacher_subject_report"),
    path('subject_reports/add', addSubjectReportView, name="add_teacher_subject_report"),
    path('subject_reports/edit/<str:pk>', editSubjectReportView,name="edit_teacher_subject_report"),
    path('subject_reports/delete/<str:pk>', deleteSubjectReportView,name="delete_teacher_subject_report"),
    path('attendance_reports/list', listAttendanceReportView,name="list_teacher_attendance_report"),
    path('attendance_reports/add',addAttendanceReportView,name="add_teacher_attendance_report"),
    path('attendance_reports/edit/<str:pk>',editAttendanceReportView,name="edit_teacher_attendance_report"),
    path('attendance_reports/delete/<str:pk>',deleteAttendanceReportView,name="delete_teacher_attendance_report"),
    #responses
    # JSON responses
    path('json/get/departments/<teacherpk>', getTeacherDepartments, name="get_teacher_departments"),
    path('json/get/students/<departmentpk>', getTeacherStudents, name="get_teacher_students"),
]