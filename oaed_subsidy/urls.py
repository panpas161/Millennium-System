from django.urls import path
from .views import *

urlpatterns =[
    path('subsidized/list',listSubsidizedIndividualView,name="list_oaed_subsidized_individuals"),
    path('subsidized/add',addSubsidizedIndividualView,name="add_oaed_subsidized_individual"),
    path('subsidized/edit/<pk>',editSubsidizedIndividualView,name="edit_oaed_subsidized_individual"),
    path('subsidized/delete/<pk>',deleteSubsidizedIndividualView,name="delete_oaed_subsidized_individual"),
    path('subsidized/view/<pk>',viewSubsidizedIndividualView,name="view_oaed_subsidized_individual"),
    #departments
    path('departments/list',listDepartmentView,name="list_oaed_subsidy_departments"),
    path('departments/add',addDepartmentView,name="add_oaed_subsidy_department"),
    path('departments/edit/<pk>',editDepartmentView,name="edit_oaed_subsidy_department"),
    path('departments/delete/<pk>',deleteDepartmentView,name="delete_oaed_subsidy_department"),
    path('departments/schedule/view/<pk>',viewScheduleDepartmentView,name="view_schedule_oaed_subsidy_department"),
    path('departments/schedule/create/<pk>',createScheduleDepartmentView,name="create_schedule_oaed_subsidy_department"),
    path('departments/schedule/edit/<pk>',editScheduleDepartmentView,name="edit_schedule_oaed_subsidy_department"),
]