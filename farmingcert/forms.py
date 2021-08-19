from .models import *
from django.forms import ModelForm

class FarmerForm(ModelForm):
    class Meta:
        model = Farmer
        fields = "__all__"

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'