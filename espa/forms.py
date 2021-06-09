from django.forms.models import ModelForm
from django import forms
from .models import *

class InterestedBusinessForm(ModelForm):
    class Meta:
        model = InterestedBusiness
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {
            'phonenumber': forms.NumberInput(),
            'cellphone': forms.NumberInput()
        }

class SubsidizedBusinessForm(ModelForm):
    class Meta:
        model = SubsidizedBusiness
        fields = '__all__'
        exclude = ['user','entrydate']
        widgets = {
            'phonenumber':forms.NumberInput(),
            'cellphone':forms.NumberInput()
        }

class EspaServiceForm(ModelForm):
    class Meta:
        model = EspaService
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {}

class UploadDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['inspected','company','entrydate']
        widgets = {}

class UploadBackendDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {}

class EspaAssociateForm(ModelForm):
    class Meta:
        model = EspaAssociate
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {}