from django.contrib.auth.models import Group
from administrator.models import Administrator
from staff.models import Staff
from students.models import Student
from teachers.models import Teacher
from espa.models import SubsidizedBusiness,EspaAssociate
from associate.models import Associate

#All roles available here
ROLES = {
    0: {
        'Name':'Admin',
        'Group':'Administrator',
        'Model':Administrator,
        'HomePage':'home',
        'isStaff':True,
        'isAdmin':True
    },
    1: {
        'Name':'Staff',
        'Group':'Staff',
        'Model':Staff,
        'HomePage':'home',
        'isStaff':True,
        'isAdmin':False
    },
    2: {
        'Name':'Student',
        'Group':'Student',
        'Model':Student,
        'HomePage':'students_front_home',
        'isStaff':False,
        'isAdmin':False
    },
    3: {
        'Name':'Teacher',
        'Group':'Teacher',
        'Model':Teacher,
        'HomePage':'teacher_home_page',
        'isStaff': False,
        'isAdmin': False
    },
    4: {
        'Name':'EspaUser',
        'Group':'EspaUser',
        'Model':SubsidizedBusiness,
        'HomePage':'espa_home',
        'isStaff': False,
        'isAdmin': False
    },
    5: {
        'Name':'Associate',
        'Group':'Associate',
        'Model':Associate,
        'HomePage':'list_interested_businesses',
        'isStaff': False,
        'isAdmin': False
    },
    6: {
        'Name':'EspaAssociate',
        'Group':'EspaAssociate',
        'Model':EspaAssociate,
        'HomePage':'list_interested_businesses',
        'isStaff': False,
        'isAdmin': False
    },
}

#Add admin roles here

ADMIN_ROLES = [
    "Admin"
]

#Add staff roles here
STAFF_ROLES = [
    "Admin",
    "Staff"
]

#Add role translations here
TRANSLATED_ROLES = {
    "Student":"Σπουδαστής",
    "Teacher":"Καθηγητής",
    "Staff":"Προσωπικό",
    "Admin":"Διαχειριστής",
    "EspaUser":"Επιδοτούμενος ΕΣΠΑ",
    "EspaAssociate":"Συνεργάτης ΕΣΠΑ",
    "Associate":"Συνεργάτης",
}

#Groups here will be created automatically(login.models)
INITIAL_GROUPS = [
    "Administrator",
    "Staff",
    "Student",
    "Teacher",
    "EspaUser",
    "EspaAssociate",
    "Associate"
]