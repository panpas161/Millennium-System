from django.forms import ModelForm
from .models import Teacher,SubjectReport
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

class SubjectReportModelForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(SubjectReportModelForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = SubjectReport
        fields = "__all__"