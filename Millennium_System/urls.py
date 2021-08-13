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
from administrator import views as adminviews
from Millennium_System import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainviews.homeView, name="home"),
    #------------LOGIN APP------------
    path('login', loginviews.loginView, name="login"),
    path('logout', loginviews.logoutView, name="logout"),
    path('profile/', include("login.urls")),
    #------------ADMINISTRATOR APP------------
    path('admin/home',adminviews.homePageView,name="admin_home"),
    #users
    path('admin/users/list/',adminviews.listUsersView,name="admin_list_users"),
    path('admin/users/add/<str:pk>',adminviews.addUserView,name="admin_add_user"),
    path('admin/users/edit/<str:pk>',adminviews.editUserView,name="admin_edit_user"),
    #----------REST----------
    path('students/',include("students.urls")),
    path('teachers/',include("teachers.urls")),
    path('cash_register/',include("cash_register.urls")),
    path('robotics/',include("robotics.urls")),
    path('farmers/',include("farmingcert.urls")),
    path('efet/',include("efet.urls")),
    path('blankpixel/',include("blankpixel.urls")),
    path('espa/',include("espa.urls")),
    path('landing/',include("landing_page.urls")),
    path('oaed/',include("oaed_subsidy.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.IMAGES_URL,document_root=settings.IMAGES_ROOT) + \
    static(settings.STYLE_URL,document_root=settings.STYLE_ROOT) + \
    static(settings.SCRIPT_URL,document_root=settings.SCRIPT_ROOT) + \
    static(settings.BOOTSTRAP_URL,document_root=settings.BOOTSTRAP_ROOT) + \
    static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(static(settings.IMAGES_URL,document_root=settings.IMAGES_ROOT) + \
#     static(settings.STYLE_URL,document_root=settings.STYLE_ROOT) + \
#     static(settings.SCRIPT_URL,document_root=settings.SCRIPT_ROOT) + \
#     static(settings.BOOTSTRAP_URL,document_root=settings.BOOTSTRAP_ROOT) + \
#     static(settings.STATIC_URL,document_root=settings.STATIC_ROOT))