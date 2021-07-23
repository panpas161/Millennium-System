from django.forms import ModelForm
from .models import *
from django import forms
from Millennium_System import settings

class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['voucher', 'studentimage', 'user', 'entrydate']
        widgets = {
            'specialty':forms.CheckboxSelectMultiple(),
            'phonenumber':forms.NumberInput(),
            'cellphone':forms.NumberInput(),
            'entrydate':forms.DateInput(format=settings.DATE_FORMAT),
            'birthdate':forms.DateInput(format=settings.DATE_FORMAT)
        }

class StudentUploadPictureForm(ModelForm):
    class Meta:
        model = Student
        fields = ['studentimage']

class SpecialtyModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SpecialtyModelForm,self).__init__(*args,**kwargs)#maybe not required
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Specialty
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {
            'entrydate':forms.HiddenInput(),
            'phonenumber':forms.NumberInput()
        }

class StudentSpecialtyForm(ModelForm):
    class Meta:
        model = StudentSpecialty
        fields = ['specialty', 'discount']

class VoucherModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(VoucherModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Voucher
        fields = '__all__'
        exclude = ['student','entrydate']
        widgets = {
            'birthdate':forms.DateInput(format=settings.DATE_FORMAT),
            'entrydate':forms.DateInput(format=settings.DATE_FORMAT)
        }

class DepartmentModelForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {
            'start_time':forms.TimeInput(attrs={
                'type':'time'
            }),
            'end_time':forms.TimeInput(attrs={
                'type':'time'
            })
        }

class ExamGradeForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(ExamGradeForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = ExamGrade
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {

        }

class GeneralSettingsForm(forms.Form):
    email = forms.CharField()

class ChangePassword(forms.Form):
    password = forms.CharField()
    confirm_password = forms.CharField()