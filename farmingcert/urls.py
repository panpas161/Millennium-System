from django.urls import path
from .views import *

urlpatterns = [
    path('list',listFarmers,name="list_farmers"),
    path('add',addFarmer,name="add_farmer"),
    path('edit',editFarmer,name="edit_farmer"),
    path('delete',deleteFarmer,name="delete_farmer"),
]