from django.db import models
from options.models import Doy,Prefecture,EducationLevel

class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    fathersname = models.CharField(max_length=30)
    mothersname = models.CharField(max_length=30)
    sex = models.CharField(max_length=30,choices=(("Άνδρας","Άνδρας"),("Γυναίκα","Γυναίκα")))
    birthdate = models.DateField(null=True,blank=True)
    afm = models.CharField(max_length=30)
    doy = models.ForeignKey(Doy,on_delete=models.CASCADE,related_name="security_expert_student")
    adt = models.CharField(max_length=30)
    issuing_authority = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    tk = models.CharField(max_length=30)
    prefecture = models.ForeignKey(Prefecture,on_delete=models.CASCADE,related_name="security_expert_student")
    mobile = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    education_level = models.ForeignKey(EducationLevel,on_delete=models.CASCADE,related_name="security_expert_student")
    companyname = models.CharField(max_length=30)
    companytype = models.CharField(max_length=30)
    employees = models.IntegerField()
    category = models.CharField(max_length=30,choices=(("Α' Κατηγορία","Α Κατηγορία"),("Β' Κατηγορία","Β' Κατηγορία"),("Γ' Κατηγορία","Γ' Κατηγορία")))
    entrydate = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    code = models.CharField(max_length=30)
    first_day_date = models.DateField()
    second_day_date = models.DateField(null=True,blank=True)
    location = models.CharField(max_length=30)
    classroom = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)
    # first_teacher = models.ForeignKey()
    # second_teacher = models.ForeignKey()
    # first_substitute_teacher = models.ForeignKey()
    # second_substitute_teacher = models.ForeignKey()