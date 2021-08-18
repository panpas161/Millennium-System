from django.forms.models import ModelForm
from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = "__all__"