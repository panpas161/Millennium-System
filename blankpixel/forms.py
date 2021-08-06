from .models import *
from django import forms
from Millennium_System import settings

class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['services','entrydate']
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

    class Meta:
        model = Price
        fields = '__all__'
        exclude = ['client']
        widgets = {
            'service':forms.HiddenInput()
        }

    def is_valid(self):
        valid = super().is_valid()
        if valid and self.cleaned_data['servicecheck']:
            return True
        return False

class InstallmentForm(forms.Form):
    payment_in_advance = forms.IntegerField(initial=0,required=True)
    total_installments = forms.IntegerField(initial=1,required=True)

    def save(self,client):
        payment_in_advance = self.cleaned_data['payment_in_advance']
        total_installments = self.cleaned_data['total_installments']
        total_price = client.getTotalCost()
        amount_per_installment = (total_price-payment_in_advance)/total_installments
        #save payment in advance
        Installment(
            client=client,
            payment_number=0,
            amount=payment_in_advance
        ).save()
        # Save the rest of the installments
        for i in range(0, total_installments):
            Installment(
                client=client,
                payment_number=i+1,
                amount=amount_per_installment
            ).save()

MultiServicesForm = forms.formset_factory(PriceForm,extra=1)