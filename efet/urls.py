from django.urls import path
from .views import *

urlpatterns = [
    #students
    path('students/list', listStudents, name="list_efet_students"),
    path('students/add', addStudent, name="add_efet_student"),
    path('students/edit/<str:pk>', editStudent,name="edit_efet_students"),
    path('students/delete/<str:pk>', deleteStudent,name="delete_efet_students"),
    #businesses
    path('business/list',listBusinessesView,name="list_efet_businesses"),
    path('business/add',addBusinessView,name="add_efet_business"),
    path('business/edit/<str:pk>',editBusinessView,name="edit_efet_business"),
    path('business/delete/<str:pk>',deleteBusinessView,name="delete_efet_business"),
]