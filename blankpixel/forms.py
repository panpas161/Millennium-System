from .models import *
from django import forms
from Millennium_System import settings

class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {
            'entrydate':forms.DateInput(format=settings.DATE_FORMAT)
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {
            'entrydate':forms.DateInput(format=settings.DATE_FORMAT)
        }

class PriceForm(forms.ModelForm):
    servicecheck = forms.BooleanField(required=False)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.empty_permitted = False

    class Meta:
        model = Price
        fields = '__all__'
        exclude = ['client']

    def is_valid(self):
        valid = super().is_valid()
        if valid and self.cleaned_data['servicecheck']:
            return True
        return False

MultiServicesForm = forms.formset_factory(PriceForm,extra=1)