from django.urls import path
from .views import *

urlpatterns = [
    path('list',listFarmers,name="list_farmers"),
    path('add',addFarmer,name="add_farmer"),
    path('edit',editFarmer,name="edit_farmer"),
    path('delete',deleteFarmer,name="delete_farmer"),
    path('departments/list',listDeparments,name="list_farming_departments"),
    path('departments/add',addDepartment,name="add_farming_department"),
    path('departments/edit/<pk>',editDepartment,name="edit_farming_department"),
    path('departments/delete/<pk>',deleteDepartment,name="delete_farming_department")
]