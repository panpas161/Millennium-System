from django.urls import path
from .views import *

urlpatterns = [
    path('espa/',espaMainView,name="landing_espa_main"),
    path('espa/register',espaRegisterView,name="landing_espa_register"),
]