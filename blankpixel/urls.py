from django.urls import path
from .views import *

urlpatterns = [
    #clients
    path('clients/list',listClientsView,name="list_blankpixel_clients"),
    path('clients/add',addClientView,name="add_blankpixel_client"),
    path('clients/edit/<pk>',editClientView,name="edit_blankpixel_client"),
    path('clients/delete/<pk>',deleteClientView,name="delete_blankpixel_client"),
    path('clients/view/services/<pk>',viewClientServicesView,name="view_blankpixel_client_services"),
    path('clients/services/mark/finished/<pk>',markServiceFinishedView,name="change_blankpixel_service_finished"),
    path('clients/services/mark/unfinished/<pk>',markServiceUnfinishedView,name="change_blankpixel_service_unfinished"),
    path('clients/view/installments/<pk>',viewClientInstallmentsView,name="view_blankpixel_client_installments"),
    path('clients/installments/pay/<pk>',payInstallmentReceiptView,name="pay_blankpixel_installment"),
    path('clients/assign/service/<pk>',assignClientServiceView,name="assign_blankpixel_client_service"),
    path('clients/deassign/service/<pk>',deassignClientServiceView,name="deassign_blankpixel_client_service"),
    # path('clients/installments/disapprove/<pk>',disapproveInstallmentView,name="disapprove_blankpixel_installments"),
    #services
    path('services/list',listServicesView,name="list_blankpixel_services"),
    path('services/add',addServiceView,name="add_blankpixel_service"),
    path('services/edit/<pk>',editServiceView,name="edit_blankpixel_service"),
    path('services/delete/<pk>',deleteServiceView,name="delete_blankpixel_service"),
    #domains
    path('domains/list',listDomainsView,name="list_blankpixel_domains"),
    #JSON
    path('get/services',getServices,name="get_blankpixel_services")
]