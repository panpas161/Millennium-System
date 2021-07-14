from django.forms.models import ModelForm
from django import forms
from .models import *

class SubsidizedIndividualForm(ModelForm):
    class Meta:
        model = SubsidizedIndividual
        fields = '__all__'
        widgets = {
            'tk':forms.NumberInput(),
            'oaed_id':forms.NumberInput(),
            'beneficiary_id':forms.NumberInput()
        }

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {

        }