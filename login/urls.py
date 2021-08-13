from django.urls import path
from .views import *

urlpatterns = [
    path('',viewProfile,name="view_profile"),
    path('settings',generalSettingsView,name="profile_settings"),
    path('change-password',changePasswordView,name="change-password")
]