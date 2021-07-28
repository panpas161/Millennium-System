"""Millennium_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views as loginviews
from main import views as mainviews
from students import views as studentviews
from cash_register import views as cashregisterviews
from blankpixel import views as blankpixelviews
from administrator import views as adminviews
from robotics import views as roboticviews
from efet import views as efetviews
from farmingcert import views as farmingviews
from espa import views as espaviews
from teachers import views as teacherviews
from landing_page import views as landingviews
from general_settings import views as gensettingsview
from oaed_subsidy import views as oaedsubsidyviews
from Millennium_System import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainviews.homeView, name="home"),
    #------------LOGIN APP------------
    path('login/', loginviews.loginView, name="login"),
    path('logout', loginviews.logoutView, name="logout"),\
    #------------ADMINISTRATOR APP------------
    path('admin/home',adminviews.homePageView,name="admin_home"),
    #users
    path('admin/users/list/',adminviews.listUsersView,name="admin_list_users"),
    path('admin/users/add/<str:pk>',adminviews.addUserView,name="admin_add_user"),
    path('admin/users/edit/<str:pk>',adminviews.editUserView,name="admin_edit_user"),
    #------------GENERAL_SETTINGS APP------------
    path('settings/profile/main',gensettingsview.showProfileView,name="show_profile"),
    path('settings/profile/edit',gensettingsview.editProfileView,name="edit_profile"),
    #------------STUDENTS APP(backend)------------
    path('students/list/', studentviews.listStudentsView, name="list-students"),
    path('students/add/', studentviews.addStudentView, name="add-student"),
    path('students/edit/<str:pk>/', studentviews.editStudentView, name="edit-student"),
    path('students/delete/<str:pk>', studentviews.deleteStudentView, name="delete-student"),
    path('students/upload/picture/<pk>', studentviews.uploadStudentPicture, name="upload_student_photo"),
    #contracts etc.
    path('students/economic_contract/<str:pk>', studentviews.economicContractView,name='economic_contract'),
    path('students/student_card/<str:pk>', studentviews.studentCardView, name="student_card"),
    path('students/installments_tab/<str:pk>',studentviews.installmentsTabView, name="installments_tab"),
    path('students/certificates/menu/<pk>',studentviews.printCertificateMenuView, name="print_students_certificate_menu"),
    path('students/certificates/seminar/<pk>',studentviews.printSeminarCertificateView, name="print_students_seminar_certificate"),
    path('students/certificates/commendation/<pk>',studentviews.printCommendationCertificateView, name="print_students_commendation_certificate"),
    path('students/certificates/praise/<pk>',studentviews.printPraiseCertificateView, name="print_students_praise_certificate"),
    #specialties
    path('students/specialties/list/', studentviews.listSpecialtiesView, name="list_student_specialties"),
    path('students/specialties/add/', studentviews.addSpecialtiesView, name="add_student_specialty"),
    path('students/specialties/edit/<str:pk>', studentviews.editSpecialtiesView, name="edit_student_specialty"),
    path('students/specialties/delete/<str:pk>',studentviews.deleteSpecialtyView,name="delete_student_specialty"),
    #departments
    path('students/departments/list', studentviews.listDepartmentsView, name="list_student_departments"),
    path('students/departments/add', studentviews.addDepartmentView, name="add_student_department"),
    path('students/departments/edit/<str:pk>', studentviews.editDepartmentView, name="edit_student_department"),
    path('students/departments/delete/<str:pk>', studentviews.deleteDepartmentView, name="delete_student_department"),
    path('students/departments/schedules/create/<pk>', studentviews.createDepartmentScheduleView, name="create_student_department_schedule"),
    #------------STUDENTS APP(frontend)------------
    #students
    path('students/home/',studentviews.mainStudentView, name="students_front_home"),
    path('students/installments/', studentviews.installmentsFrontTabView, name="students_front_installments"),
    path('students/exams/',studentviews.examsStudentView,name="student_front_exams_tab"),
    #settings
    path('students/settings/general',studentviews.examsStudentView,name="student_settings_general"),
    #------------TEACHERS APP------------
    # backend
    path('teachers/list/', teacherviews.listTeachersView, name="list_teachers"),
    path('teachers/add/', teacherviews.addTeacherView, name="add_teacher"),
    path('teachers/edit/<str:pk>', teacherviews.editTeacherView, name="edit_teacher"),
    path('teachers/delete/<str:pk>', teacherviews.deleteTeacherView, name="delete_teacher"),
    path('teachers/credentials/create/<str:pk>', teacherviews.createTeacherCredentials, name="create_teacher_credentials"),
    path('teachers/credentials/create/new/<str:pk>', teacherviews.recreateTeacherCredentials, name="recreate_teacher_credentials"),
    #frontend
    path('teachers/home/', teacherviews.teacherHomeView, name="teacher_home_page"),
    path('teachers/exams/add/', teacherviews.addExamGradeView, name="add_teacher_grades"),
    path('teachers/exams/edit/<pk>', teacherviews.editExamGradeView, name="edit_teacher_grades"),
    path('teachers/exams/list', teacherviews.listExamGradeView, name="list_teacher_exams"),
    path('teachers/subject_reports/list', teacherviews.listSubjectReportView, name="list_teacher_subject_report"),
    path('teachers/subject_reports/add', teacherviews.addSubjectReportView, name="add_teacher_subject_report"),
    path('teachers/subject_reports/edit/<str:pk>', teacherviews.editSubjectReportView,name="edit_teacher_subject_report"),
    path('teachers/subject_reports/delete/<str:pk>', teacherviews.deleteSubjectReportView,name="delete_teacher_subject_report"),
    path('teachers/attendance_reports/list', teacherviews.listAttendanceReportView,name="list_teacher_attendance_report"),
    path('teachers/attendance_reports/add',teacherviews.addAttendanceReportView,name="add_teacher_attendance_report"),
    path('teachers/attendance_reports/edit/<str:pk>',teacherviews.editAttendanceReportView,name="edit_teacher_attendance_report"),
    path('teachers/attendance_reports/delete/<str:pk>',teacherviews.deleteAttendanceReportView,name="delete_teacher_attendance_report"),
    #------------CASH_REGISTER APP------------
    #receipts
    path('cash_register/receipts/list/',cashregisterviews.listReceiptsView,name="list_receipts"),
    path('cash_register/receipts/add',cashregisterviews.addReceiptView,name="add_receipt"),
    path('cash_register/receipts/edit/<str:pk>',cashregisterviews.editReceiptView,name="edit_receipt"),
    path('cash_register/receipts/delete/<str:pk>',cashregisterviews.deleteReceiptView,name="delete_receipt"),
    #expenses
    path('cash_register/expenses/list',cashregisterviews.listExpensesView,name="list_expenses"),
    path('cash_register/expenses/add', cashregisterviews.addExpenseView,name="add_expense"),
    path('cash_register/expenses/edit/<str:pk>',cashregisterviews.editExpenseView,name="edit_expense"),
    path('cash_register/expenses/delete/<str:pk>',cashregisterviews.deleteExpenseView,name="delete_expense"),
    #register
    path('cash_register/overview',cashregisterviews.registerOverviewView,name="register_overview"),
    #------------ROBOTICS APP------------
    path('robotics/students/list',roboticviews.listRoboticStudents,name="list_robotic_students"),
    path('robotics/students/add',roboticviews.addRoboticStudent,name="add_robotic_student"),
    path('robotics/students/edit/<str:pk>',roboticviews.editRoboticStudent,name="edit_robotic_students"),
    path('robotics/students/delete/<str:pk>',roboticviews.deleteRoboticStudent,name="delete_robotic_students"),
    #------------SECURITYEXPERTS APP------------
    path('farmers/list',farmingviews.listFarmers,name="list_farmers"),
    path('farmers/add',farmingviews.addFarmer,name="add_farmer"),
    path('farmers/edit',farmingviews.editFarmer,name="edit_farmer"),
    path('farmers/delete',farmingviews.deleteFarmer,name="delete_farmer"),
    #------------EFET APP------------
    #students
    path('efet/students/list', efetviews.listStudents, name="list_efet_students"),
    path('efet/students/add', efetviews.addStudent, name="add_efet_student"),
    path('efet/students/edit/<str:pk>', efetviews.editStudent,name="edit_efet_students"),
    path('efet/students/delete/<str:pk>', efetviews.deleteStudent,name="delete_efet_students"),
    #businesses
    path('efet/business/list',efetviews.listBusinessesView,name="list_efet_businesses"),
    path('efet/business/add',efetviews.addBusinessView,name="add_efet_business"),
    path('efet/business/edit/<str:pk>',efetviews.editBusinessView,name="edit_efet_business"),
    path('efet/business/delete/<str:pk>',efetviews.deleteBusinessView,name="delete_efet_business"),
    #------------BLANKPIXEL APP------------
    #clients
    path('blankpixel/clients/list',blankpixelviews.listClientsView,name="list_blankpixel_clients"),
    path('blankpixel/clients/add',blankpixelviews.addClientView,name="add_blankpixel_client"),
    path('blankpixel/clients/edit/<pk>',blankpixelviews.editClientView,name="edit_blankpixel_client"),
    path('blankpixel/clients/delete/<pk>',blankpixelviews.deleteClientView,name="delete_blankpixel_client"),
    #services
    path('blankpixel/services/list',blankpixelviews.listServicesView,name="list_blankpixel_services"),
    path('blankpixel/services/add',blankpixelviews.addServiceView,name="add_blankpixel_service"),
    path('blankpixel/services/edit/<pk>',blankpixelviews.editServiceView,name="edit_blankpixel_service"),
    path('blankpixel/services/delete/<pk>',blankpixelviews.deleteServiceView,name="delete_blankpixel_service"),
    #domains
    path('blankpixel/domains/list',blankpixelviews.listDomainsView,name="list_blankpixel_domains"),
    #------------ESPA APP------------
    #Backend
    #interested
    path('espa/interested/list',espaviews.listInterestedBusinessesView,name="list_espa_interested_businesses"),
    path('espa/interested/add',espaviews.addInterestedBusinessView,name="add_espa_interested_business"),
    path('espa/interested/edit/<pk>',espaviews.editInterestedBusinessView,name="edit_espa_interested_business"),
    path('espa/interested/delete/<pk>',espaviews.deleteInterestedBusinessView,name="delete_espa_interested_business"),
    path('espa/interested/view/<pk>', espaviews.viewInterestedBusinessView, name="view_espa_interested_business"),
    path('espa/interested/approve/<pk>',espaviews.approveInterestedBusiness,name="approve_espa_interested_business"),
    #subsidized
    path('espa/businesses/list',espaviews.listSubsidizedBusinessView,name="list_espa_subsidized_businesses"),
    path('espa/businesses/add',espaviews.addSubsidizedBusinessView,name="add_espa_subsidized_business"),
    path('espa/businesses/edit/<pk>',espaviews.editSubsidizedBusinessView,name="edit_espa_subsidized_business"),
    path('espa/businesses/delete/<pk>',espaviews.deleteSubsidizedBusinessView,name="delete_espa_subsidized_business"),
    path('espa/businesses/view/<pk>',espaviews.viewSubsidizedBusinessView,name="view_espa_subsidized_business"),
    path('espa/businesses/documents/<pk>',espaviews.documentsSubsidizedBusinessView,name="documents_espa_subsidized_businesses"),
    path('espa/businesses/documents/inspect/<pk>',espaviews.inspectDocumentView,name="inspect_espa_business_document"),
    path('espa/businesses/documents/delete/<pk>',espaviews.deleteDocument,name="delete_espa_business_document"),
    path('espa/businesses/documents/add/<pk>',espaviews.addDocumentView,name="add_espa_business_document"),
    path('espa/businesses/credentials/create/<pk>',espaviews.createEspaUserCredentials,name="create_espa_user_credentials"),
    #services
    path('espa/services/list',espaviews.listServicesView,name="list_espa_services"),
    path('espa/services/add',espaviews.addServiceView,name="add_espa_service"),
    path('espa/services/edit/<pk>',espaviews.editServiceView,name="edit_espa_service"),
    path('espa/services/delete/<pk>',espaviews.deleteServiceView,name="delete_espa_service"),
    #espa_associates
    path('espa/associates/list/',espaviews.listEspaAssociatesView,name="list_espa_associates"),
    path('espa/associates/add/',espaviews.addEspaAssociateView,name="add_espa_associate"),
    path('espa/associates/edit/<pk>',espaviews.editEspaAssociateView,name="edit_espa_associate"),
    path('espa/associates/delete/<pk>',espaviews.deleteEspaAssociateView,name="delete_espa_associate"),
    path('espa/associates/credentials/create/<pk>',espaviews.createEspaAssociateCredentials,name="create_espa_associate_creds"),
    path('espa/associates/credentials/remove/<pk>',espaviews.removeEspaAssociateCredentials,name="remove_espa_associate_creds"),
    #Frontend
    path('espa/home',espaviews.homePageView,name="espa_home"),
    path('espa/documents/list',espaviews.listDocuments,name="espauser_list_documents"),
    path('espa/documents/upload',espaviews.uploadDocuments,name="espa_upload_documents"),
    #------------LANDING PAGES APP------------
    path('landing/espa/',landingviews.espaMainView,name="landing_espa_main"),
    path('landing/espa/register',landingviews.espaRegisterView,name="landing_espa_register"),
    #------------OAED_SUBSIDY APP------------
    path('oaed/subsidized/list',oaedsubsidyviews.listSubsidizedIndividualView,name="list_oaed_subsidized_individuals"),
    path('oaed/subsidized/add',oaedsubsidyviews.addSubsidizedIndividualView,name="add_oaed_subsidized_individual"),
    path('oaed/subsidized/edit/<pk>',oaedsubsidyviews.editSubsidizedIndividualView,name="edit_oaed_subsidized_individual"),
    path('oaed/subsidized/delete/<pk>',oaedsubsidyviews.deleteSubsidizedIndividualView,name="delete_oaed_subsidized_individual"),
    path('oaed/subsidized/view/<pk>',oaedsubsidyviews.viewSubsidizedIndividualView,name="view_oaed_subsidized_individual"),
    #departments
    path('oaed/departments/list',oaedsubsidyviews.listDepartmentView,name="list_oaed_subsidy_departments"),
    path('oaed/departments/add',oaedsubsidyviews.addDepartmentView,name="add_oaed_subsidy_department"),
    path('oaed/departments/edit/<pk>',oaedsubsidyviews.editDepartmentView,name="edit_oaed_subsidy_department"),
    path('oaed/departments/delete/<pk>',oaedsubsidyviews.deleteDepartmentView,name="delete_oaed_subsidy_department"),
    path('oaed/departments/schedule/view/<pk>',oaedsubsidyviews.viewScheduleDepartmentView,name="view_schedule_oaed_subsidy_department"),
    path('oaed/departments/schedule/create/<pk>',oaedsubsidyviews.createScheduleDepartmentView,name="create_schedule_oaed_subsidy_department"),
    path('oaed/departments/schedule/edit/<pk>',oaedsubsidyviews.editScheduleDepartmentView,name="edit_schedule_oaed_subsidy_department"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.IMAGES_URL,document_root=settings.IMAGES_ROOT) + \
    static(settings.STYLE_URL,document_root=settings.STYLE_ROOT) + \
    static(settings.SCRIPT_URL,document_root=settings.SCRIPT_ROOT) + \
    static(settings.BOOTSTRAP_URL,document_root=settings.BOOTSTRAP_ROOT) + \
    static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)