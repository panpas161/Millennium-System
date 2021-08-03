from django.urls import path
from .views import *

urlpatterns = [
    path('students/list',listRoboticStudents,name="list_robotic_students"),
    path('students/add',addRoboticStudent,name="add_robotic_student"),
    path('students/edit/<str:pk>',editRoboticStudent,name="edit_robotic_students"),
    path('students/delete/<str:pk>',deleteRoboticStudent,name="delete_robotic_students"),
]