from login.models import User
from students.models import Student

def getUserID(username):
    userinstance = User.objects.get(username=username)
    return userinstance.id

def getStudentID(username):
    studentinstance = Student.objects.get(user=username)
    return studentinstance.id

#to be moved to assets/functions