from django.contrib.auth.models import User
from students.models import Student

def getUserID(username):
    userinstance = User.objects.get(username=username)
    return userinstance.id

def getStudentID(username):
    studentinstance = Student.objects.get(user=username)
    return studentinstance.id

#Above are TBD(to be deleted)
def getUserModelID(model,username):
    userinstance = model.objects.get(user=username)
    return userinstance.id