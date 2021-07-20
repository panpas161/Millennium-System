from django.template.loader import render_to_string
from django import template
from django.contrib import messages
from assets.functions.authentication import getUserRoles,translateUserRole
from assets.functions.authentication import isStaff

register = template.Library()
#students
@register.simple_tag(name="renderStudentFrontendNavbar")
def studentFrontendNavbarView(request):
    template = 'Frontend/Navbar/frontend_students_navbar.html'
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {

        'usertype':usertype,
        'request':request,
        'messages': messages.get_messages(request)
    }
    #render the template
    return render_to_string(template, data)

@register.simple_tag(name="renderStudentBackendNavbar")
def studentBackendNavbarView(request):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {
        'usertype':usertype,
        'request':request,
        'messages': messages.get_messages(request)
    }
    return render_to_string("Backend/Navbar/navbar_students.html",data)

#cash_register
@register.simple_tag(name="renderRegisterBackendNavbar")
def cashRegisterBackendNavbarView(request):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {
        'usertype':usertype,
        'request':request,
        'messages': messages.get_messages(request)
    }
    return render_to_string("Backend/Navbar/main_navbar.html",data)

@register.simple_tag(name="renderBlankpixelNavbar")
def blankpixelNavbarView(request):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {
        'usertype':usertype,
        'request':request,
        'messages': messages.get_messages(request)
    }
    return  render_to_string("Backend/Navbar/blankpixel_navbar_one.html",data)

@register.simple_tag(name="renderEfetNavbar")
def efetNavbarView(request):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data  ={

        'usertype':usertype,
        'request':request,
        'messages': messages.get_messages(request)
    }
    return render_to_string("Navbar/efet_navbar_one.html",data)
@register.simple_tag(name="renderTeacherBackendNavbar")
def teacherBackendNavbarView(request):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {

        'usertype':usertype,
        'request':request,
        'messages': messages.get_messages(request)
    }
    return render_to_string("Backend/Navbar/teachers_navbar.html",data)

@register.simple_tag(name="renderTeacherFrontendNavbar")
def teacherFrontendNavbarView(request):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {

        'usertype':usertype,
        'request':request,
        'messages': messages.get_messages(request)
    }
    return render_to_string("Teachers_Frontend/Navbar/navbar.html",data)

@register.simple_tag(name="renderEspaBackendNavbar")
def espaBackendNavbarView(request):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {
        'usertype':usertype,
        'request':request,
        'messages':messages.get_messages(request),
        'isStaff':isStaff(request),
    }
    return render_to_string("Espa_Backend/Navbar/espa_backend_navbar.html",data)

@register.simple_tag(name="renderEspaFrontendNavbar")
def espaFrontendNavbarView(request):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {

        'usertype':usertype,
        'request':request,
        'companyname':request.user.subsidizedbusiness.companyname,
        'messages': messages.get_messages(request),
    }
    return render_to_string("Espa_Frontend/Navbar/espa_frontend_navbar.html",data)\

@register.simple_tag(name="renderOaedSubsidyBackendNavbar")
def oaedSubsidyBackendNavbarView(request):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {

        'usertype':usertype,
        'request':request,
        'messages': messages.get_messages(request),
    }
    return render_to_string("Backend/Oaed_Navbar/backend_navbar.html",data)

@register.simple_tag(name="renderProfileNavbar")
def profileNavbarView(request):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {
        'usertype':usertype
    }
    return render_to_string("Profiles/navbar.html",data)

@register.simple_tag(name="renderNavbar")
def renderNavbar(request,path):
    role = getUserRoles(request)[0]
    usertype = translateUserRole(role)
    data = {
        'usertype':usertype,
        'request':request,
        'messages':messages.get_messages(request)
    }
    return render_to_string(path,data)