from django.forms.models import ModelForm
from .models import *

class EfetStudentModelForm(ModelForm):
    class Meta:
        model = EfetStudent
        fields = "__all__"

class EfetBusinessModelForm(ModelForm):
    class Meta:
        model = EfetBusiness
        fields = "__all__"