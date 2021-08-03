from django.urls import path
from .views import *

urlpatterns = [
    #Backend
    #interested
    path('interested/list',listInterestedBusinessesView,name="list_espa_interested_businesses"),
    path('interested/add',addInterestedBusinessView,name="add_espa_interested_business"),
    path('interested/edit/<pk>',editInterestedBusinessView,name="edit_espa_interested_business"),
    path('interested/delete/<pk>',deleteInterestedBusinessView,name="delete_espa_interested_business"),
    path('interested/view/<pk>', viewInterestedBusinessView, name="view_espa_interested_business"),
    path('interested/approve/<pk>',approveInterestedBusiness,name="approve_espa_interested_business"),
    #subsidized
    path('businesses/list',listSubsidizedBusinessView,name="list_espa_subsidized_businesses"),
    path('businesses/add',addSubsidizedBusinessView,name="add_espa_subsidized_business"),
    path('businesses/edit/<pk>',editSubsidizedBusinessView,name="edit_espa_subsidized_business"),
    path('businesses/delete/<pk>',deleteSubsidizedBusinessView,name="delete_espa_subsidized_business"),
    path('businesses/view/<pk>',viewSubsidizedBusinessView,name="view_espa_subsidized_business"),
    path('businesses/documents/<pk>',documentsSubsidizedBusinessView,name="documents_espa_subsidized_businesses"),
    path('businesses/documents/inspect/<pk>',inspectDocumentView,name="inspect_espa_business_document"),
    path('businesses/documents/delete/<pk>',deleteDocument,name="delete_espa_business_document"),
    path('businesses/documents/add/<pk>',addDocumentView,name="add_espa_business_document"),
    path('businesses/credentials/create/<pk>',createEspaUserCredentials,name="create_espa_user_credentials"),
    #services
    path('services/list',listServicesView,name="list_espa_services"),
    path('services/add',addServiceView,name="add_espa_service"),
    path('services/edit/<pk>',editServiceView,name="edit_espa_service"),
    path('services/delete/<pk>',deleteServiceView,name="delete_espa_service"),
    #espa_associates
    path('associates/list/',listEspaAssociatesView,name="list_espa_associates"),
    path('associates/add/',addEspaAssociateView,name="add_espa_associate"),
    path('associates/edit/<pk>',editEspaAssociateView,name="edit_espa_associate"),
    path('associates/delete/<pk>',deleteEspaAssociateView,name="delete_espa_associate"),
    path('associates/credentials/create/<pk>',createEspaAssociateCredentials,name="create_espa_associate_creds"),
    path('associates/credentials/remove/<pk>',removeEspaAssociateCredentials,name="remove_espa_associate_creds"),
    #Frontend
    path('home',homePageView,name="espa_home"),
    path('documents/list',listDocuments,name="espauser_list_documents"),
    path('documents/upload',uploadDocuments,name="espa_upload_documents"),
]