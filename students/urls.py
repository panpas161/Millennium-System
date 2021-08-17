from django.urls import path
from .views import *

urlpatterns = [
    #backend
    path('list/', listStudentsView, name="list-students"),
    path('add/', addStudentView, name="add-student"),
    path('edit/<str:pk>/', editStudentView, name="edit-student"),
    path('delete/<str:pk>', deleteStudentView, name="delete-student"),
    path('upload/picture/<pk>', uploadStudentPicture, name="upload_student_photo"),
    #contracts etc.
    path('economic_contract/<str:pk>', economicContractView,name='economic_contract'),
    path('student_card/<str:pk>', studentCardView, name="student_card"),
    path('installments_tab/<str:pk>',installmentsTabView, name="installments_tab"),
    path('certificates/menu/<pk>',printCertificateMenuView, name="print_students_certificate_menu"),
    path('certificates/seminar/<pk>',printSeminarCertificateView, name="print_students_seminar_certificate"),
    path('certificates/commendation/<pk>',printCommendationCertificateView, name="print_students_commendation_certificate"),
    path('certificates/praise/<pk>',printPraiseCertificateView, name="print_students_praise_certificate"),
    #specialties
    path('specialties/list/', listSpecialtiesView, name="list_student_specialties"),
    path('specialties/add/', addSpecialtiesView, name="add_student_specialty"),
    path('specialties/edit/<str:pk>', editSpecialtiesView, name="edit_student_specialty"),
    path('specialties/delete/<str:pk>',deleteSpecialtyView,name="delete_student_specialty"),
    path('specialties/get/specialties',getSpecialties,name="get_student_specialties"),
    path('specialties/get/prices',getSpecialtyPrices,name="get_student_specialty_prices"),
    #departments
    path('departments/list', listDepartmentsView, name="list_student_departments"),
    path('departments/add', addDepartmentView, name="add_student_department"),
    path('departments/edit/<str:pk>', editDepartmentView, name="edit_student_department"),
    path('departments/delete/<str:pk>', deleteDepartmentView, name="delete_student_department"),
    path('departments/schedules/create/<pk>', createDepartmentScheduleView, name="create_student_department_schedule"),
    #frontend
    #students
    path('home/',mainStudentView, name="students_front_home"),
    path('installments/', installmentsFrontTabView, name="students_front_installments"),
    path('exams/',examsStudentView,name="student_front_exams_tab"),
]