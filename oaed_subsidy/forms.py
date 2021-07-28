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
    def __init__(self,*args,**kwargs):
        super(DepartmentDayForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False
    class Meta:
        model = DepartmentDay
        fields = '__all__'
        exclude = ['department','entrydate']
        widgets = {
            'weekday':forms.CheckboxInput(),
            'start_time': forms.TimeInput(attrs={
                'type':'time'
            }),
            'end_time': forms.TimeInput(attrs={
                'type': 'time'
            })
        }

    # def save(self):
    #     super(self,DepartmentDayForm).save()

DepartmentDayMultipleForm = forms.formset_factory(DepartmentDayForm,extra=7)

# DepartmentDayEditMultipleForm = forms.inlineformset_factory(DepartmentDayForm,fields=("weekday",))