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
        exclude = ['specialties', 'voucher', 'studentimage', 'user', 'entrydate']
        widgets = {
            'phonenumber':forms.NumberInput(),
            'cellphone':forms.NumberInput(),
            'birthdate':forms.DateInput(format=settings.DATE_FORMAT)
        }

class StudentUploadPictureForm(ModelForm):
    class Meta:
        model = Student
        fields = ['studentimage']

class SpecialtyModelForm(ModelForm):
    class Meta:
        model = Specialty
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {
            'entrydate':forms.HiddenInput(),
            'phonenumber':forms.NumberInput()
        }

class VoucherModelForm(ModelForm):
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
        if not authorized:
            self.fields.pop("teacher")
    class Meta:
        model = ExamGrade
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {

        }

class StudentSpecialtyForm(ModelForm):
    specialtycheck = forms.BooleanField(required=False)
    class Meta:
        model = StudentSpecialty
        fields = '__all__'
        exclude = ['student']
        widgets = {
            'specialty':forms.HiddenInput(),
            'discount': forms.NumberInput(attrs={"min": 0})
        }

    def is_valid(self):
        valid = super().is_valid()
        if valid and self.cleaned_data['specialtycheck']:
            return True
        return False


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

class InstallmentForm(forms.Form):
    payment_in_advance = forms.FloatField(initial=0.0,required=True,widget=forms.NumberInput(attrs={"min":0}))
    total_installments = forms.IntegerField(initial=0,required=True,widget=forms.NumberInput(attrs={"min":0}))

    def is_valid(self):
        valid = super().is_valid()
        if valid:
            if self.cleaned_data["payment_in_advance"] > 0 and self.cleaned_data["total_installments"] >= 0 and self.cleaned_data["total_installments"] <= 24:
                return True
        return False

    def save(self,student):
        payment_in_advance = self.cleaned_data['payment_in_advance']
        total_installments = self.cleaned_data['total_installments']
        total_price = student.getTotalCost()
        if total_installments != 0:
            amount_per_installment = (total_price-payment_in_advance)/total_installments
        else:
            amount_per_installment = total_price-payment_in_advance
        #save payment in advance
        Installment(
            student=student,
            payment_number=0,
            amount=payment_in_advance
        ).save()
        # Save the rest of the installments
        for i in range(1, total_installments+1):
            Installment(
                student=student,
                payment_number=i,
                amount=amount_per_installment
            ).save()

class GeneralSettingsForm(forms.Form):
    email = forms.CharField()

class ChangePassword(forms.Form):
    password = forms.CharField()
    confirm_password = forms.CharField()

DepartmentDayMultipleForm = forms.formset_factory(DepartmentDayForm, extra=7)
MultiSpecialtiesForm = forms.formset_factory(StudentSpecialtyForm, extra=1)