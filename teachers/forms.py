from django.forms import ModelForm
from .models import *
from django import forms

class TeacherModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeacherModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'entrydate':forms.HiddenInput(),
            'phonenumber':forms.NumberInput()
        }

class SubjectReportForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(SubjectReportForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = SubjectReport
        fields = '__all__'

class AttendanceReportForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(AttendanceReportForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = AttendanceReport
        fields = '__all__'