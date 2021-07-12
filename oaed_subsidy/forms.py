from django.forms.models import ModelForm
from .models import *

class SubsidizedIndividualForm(ModelForm):
    class Meta:
        model = SubsidizedIndividual
        fields = '__all__'
        widgets = {

        }