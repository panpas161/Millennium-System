from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from students.models import Student

def addUser(username,email,password):
    user = User.objects.create_user(username=username,email=email,password=password)
    user.save()

# def addStudent(username):
#     user = Student.objects.get(user=username)
#     group = Group.objects.get(name="StudentsGroup")
#     user.groups.add(group)
#     user.save()
#
# def addTeacher(username,password):
#     user = User.objects.create_user(username=username,password=password)
#     group = Group.objects.get(name="TeachersGroup")
#     user.groups.add(group)
#     user.save()
#
# def addStaff(username,password):
#     user = User.objects.create_user(username=username,password=password)
#     group = Group.objects.get(name="StaffGroup")
#     user.groups.add(group)
#     user.save()

def changeUserPassword(username,password):
    object = User.objects.get(username=username)
    object.set_password(password)
    object.save()

def createGroup(groupname): #add permissions for more security
    group = Group.objects.filter(name=groupname)
    if not group.exists():
        Group.objects.create(name=groupname)


# def assignUser(user,group):


def assignToGroup(username,groupname):
    createGroup(groupname)
    group = Group.objects.get(name=groupname)
    user = User.objects.get(username=username)
    user.groups.add(group)
    # assignUser(user,groupname)

