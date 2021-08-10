from django.forms.models import ModelForm
from django import forms
from .models import *

class SubsidizedIndividualForm(ModelForm):
    class Meta:
        model = SubsidizedIndividual
        fields = '__all__'
        exclude = ['entrydate']
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

class DepartmentDayForm(ModelForm):
    checkday = forms.BooleanField(required=False)
    def __init__(self,*args,**kwargs):
        super(DepartmentDayForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False
        # self.fields['weekday'].initial = "test"
    class Meta:
        model = DepartmentDay
        fields = '__all__'
        exclude = ['department','entrydate']
        widgets = {
            'start_time': forms.TimeInput(attrs={
                'type':'time'
            }),
            'end_time': forms.TimeInput(attrs={
                'type': 'time'
            }),
            'weekday':forms.HiddenInput()
        }

    def is_valid(self):
        valid = super().is_valid()
        if valid:
            if self.cleaned_data['checkday']:
                return True
            return False

DepartmentDayMultipleForm = forms.formset_factory(DepartmentDayForm,extra=7)

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['entrydate']
