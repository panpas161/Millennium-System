from .models import *
from django import forms
from Millennium_System import settings

class ClientModelForm(forms.ModelForm):
    validfield = forms.BooleanField(required=False)
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {
            'entrydate':forms.DateInput(format=settings.DATE_FORMAT)
        }

    # def is_valid(self):
    #     valid = super().is_valid()
    #     if valid:
    #         if self.fields['validfield']:
    #             print(self.vali)
    #             return True
    #     else:
    #         return False

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        exclude = ['entrydate']
        widgets = {
            'entrydate':forms.DateInput(format=settings.DATE_FORMAT)
        }

class PriceForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.empty_permitted = False
    class Meta:
        model = Price
        fields = '__all__'

    def is_valid(self):
        valid = super().is_valid()
        if valid:
            if self.validfield:
                return True
        else:
            return False