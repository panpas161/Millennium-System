from django.forms import ModelForm
from .models import Staff

class StaffModelForm(ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"