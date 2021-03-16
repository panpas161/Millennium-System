from django.forms.models import ModelForm
from django import forms
from .models import *

class InterestedBusinessForm(ModelForm):
    class Meta:
        model = InterestedBusiness
        fields = '__all__'
        exclude = ['espauser']
        widgets = {
            'entrydate': forms.HiddenInput(),
            'phonenumber': forms.NumberInput(),
            'cellphone': forms.NumberInput()
        }

class SubsidizedBusinessForm(ModelForm):
    class Meta:
        model = SubsidizedBusiness
        fields = '__all__'
        exclude = ['espauser']
        widgets = {
            'entrydate':forms.HiddenInput(),
            'phonenumber':forms.NumberInput(),
            'cellphone':forms.NumberInput()
        }

class EspaServiceForm(ModelForm):
    class Meta:
        model = EspaService
        fields = '__all__'
        widgets = {
            'entrydate':forms.HiddenInput()
        }

class UploadDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['inspected','company']
        widgets = {
            'entrydate':forms.HiddenInput()
        }

class UploadBackendDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        widgets = {
            'entrydate':forms.HiddenInput
        }