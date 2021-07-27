from django.forms import ModelForm
from .models import *
from django import forms
from Millennium_System import settings
# from django.contrib.admin.widgets import FilteredSelectMultiple
from django.shortcuts import render
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
        super(SpecialtyModelForm,self).__init__(*args,**kwargs)
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

# class StudentSpecialtyForm(ModelForm):
#     class Meta:
#         model = StudentSpecialty
#         fields = ['specialty', 'discount']

class VoucherModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(VoucherModelForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False
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

class DepartmentDayForm(ModelForm):
    class Meta:
        model = DepartmentDay
        fields = '__all__'
        exclude = ['department', 'entrydate']
        widgets = {
            'start_time': forms.TimeInput(attrs={
                'type': 'time'
            }),
            'end_time': forms.TimeInput(attrs={
                'type': 'time'
            })
        }

    def __init__(self, *args, **kwargs):
        super(DepartmentDayForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False

class ExamGradeForm(ModelForm):
    def __init__(self,*args,**kwargs):
        authorized = kwargs.pop('authorized', None)
        super(ExamGradeForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        if not authorized:
            self.fields.pop("teacher")
    class Meta:
        model = ExamGrade
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {

        }

class StudentSpecialtyForm(ModelForm):
    class Meta:
        model = StudentSpecialty
        fields = '__all__'
        exclude = ['student','specialty']
    #
    # def save(self,commit=True):
    #     instance = forms.ModelForm.save(self,commit)
    #     instance.save(send=0)
    #     for specialty in self.cleaned_data['specialties']:
    #         instance.specialties.add()

class SeminarCertificateForm(forms.Form):
    sexoptions = (
        ("Άνδρας","Άνδρας"),
        ("Γυναίκα","Γυναίκα")
    )
    sex = forms.ChoiceField(choices=sexoptions)
    lastname = forms.CharField(max_length=20)
    firstname = forms.CharField(max_length=20)
    fathersname = forms.CharField(max_length=20)
    adt = forms.CharField(max_length=20)
    specialty = forms.CharField(max_length=20)
    location = forms.CharField(max_length=20)
    # dates = forms.DateField()
    lecturersex = forms.ChoiceField(choices=sexoptions)
    lecturer = forms.CharField(max_length=20)
    aa = forms.CharField(max_length=20)
    # aadate = forms.DateField()

class CommendationCertificateForm(forms.Form):
    sexoptions = (
        ("Άνδρας", "Άνδρας"),
        ("Γυναίκα", "Γυναίκα")
    )
    sex = forms.ChoiceField(choices=sexoptions)
    lastname = forms.CharField(max_length=20)
    firstname = forms.CharField(max_length=20)
    fathersname = forms.CharField(max_length=20)
    specialty = forms.CharField(max_length=20)

class PraiseCertificateForm(forms.Form):
    sexoptions = (
        ("Άνδρας", "Άνδρας"),
        ("Γυναίκα", "Γυναίκα")
    )
    sex = forms.ChoiceField(choices=sexoptions)
    lastname = forms.CharField(max_length=20)
    firstname = forms.CharField(max_length=20)
    fathersname = forms.CharField(max_length=20)
    contest = forms.CharField(max_length=20)
    contest_location = forms.CharField(max_length=20)
    date = forms.DateField()

class GeneralSettingsForm(forms.Form):
    email = forms.CharField()

class ChangePassword(forms.Form):
    password = forms.CharField()
    confirm_password = forms.CharField()