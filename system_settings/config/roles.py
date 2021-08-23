from django.contrib.auth.models import Group
from administrator.models import Administrator
from staff.models import Staff
from students.models import Student
from teachers.models import Teacher
from espa.models import SubsidizedBusiness,EspaAssociate
from associate.models import Associate

#All roles available here
try:#ignore if Group.objects.get function returns doesnotexist error
    ROLES = {
        0: {
            'Name':'Admin',
            'Group':Group.objects.get(name="Administrator"),
            'Model':Administrator,
            'HomePage':'home'
        },
        1: {
            'Name':'Staff',
            'Group':Group.objects.get(name="Staff"),
            'Model':Staff,
            'HomePage':'home'
        },
        2: {
            'Name':'Student',
            'Group':Group.objects.get(name="Student"),
            'Model':Student,
            'HomePage':'students_front_home'
        },
        3: {
            'Name':'Teacher',
            'Group':Group.objects.get(name="Teacher"),
            'Model':Teacher,
            'HomePage':'teacher_home_page'
        },
        4: {
            'Name':'EspaUser',
            'Group':Group.objects.get(name="EspaUser"),
            'Model':SubsidizedBusiness,
            'HomePage':'espa_home'
        },
        5: {
            'Name':'Associate',
            'Group':Group.objects.get(name="Associate"),
            'Model':Associate,
            'HomePage':'list_interested_businesses'
        },
        6: {
            'Name':'EspaAssociate',
            'Group':Group.objects.get(name="EspaAssociate"),
            'Model':EspaAssociate,
            'HomePage':'list_interested_businesses'
        },
    }
except:
    pass

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