from .models import *
from django import forms
from Millennium_System import settings
from cash_register.models import Receipt

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

class ClientServiceForm(forms.ModelForm):
    servicecheck = forms.BooleanField(required=False)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model = ClientService
        fields = '__all__'
        exclude = ['client']
        widgets = {
            'service':forms.HiddenInput(),
            'price':forms.NumberInput(attrs={"min":0}),
            'discount':forms.NumberInput(attrs={"min":0})
        }

    def is_valid(self):
        valid = super().is_valid()
        if valid and self.cleaned_data['servicecheck']:
            return True
        return False

class InstallmentForm(forms.Form):
    payment_in_advance = forms.FloatField(initial=0.0,required=True,widget=forms.NumberInput(attrs={"min":0}))
    total_installments = forms.IntegerField(initial=0,required=True,widget=forms.NumberInput(attrs={"min":0}))

    def is_valid(self):
        valid = super().is_valid()
        if valid:
            if self.cleaned_data["payment_in_advance"] > 0 and self.cleaned_data["total_installments"] >= 0 and self.cleaned_data['total_installments'] <= 24:
                return True
        return False

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
        for i in range(1, total_installments+1):
            Installment(
                client=client,
                payment_number=i,
                amount=amount_per_installment
            ).save()

class ReceiptForm(forms.Form):
    recipient = forms.CharField() #automatically?
    paymentmethod = forms.CharField()
    paymentway = forms.CharField()

    def save(self,client):
        client.issueReceipt(
            recp_full_name=self.cleaned_data['recipient'],
            paymentmethod=self.cleaned_data['paymentmethod'],
            paymentway=self.cleaned_data['paymentway']
        )

MultiServicesForm = forms.formset_factory(ClientServiceForm,extra=1)